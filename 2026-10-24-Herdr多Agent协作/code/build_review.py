"""Validate source assets and build a self-contained editorial preview.

Does not install software, run Herdr, or contact a model provider.
Requires the already available Python-Markdown and Pillow packages.
"""
from pathlib import Path
from html.parser import HTMLParser
import base64
import hashlib
import json
import re
import zipfile
import markdown
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]

class ImageEmbedder(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.parts = []
        self.image_count = 0
    def handle_starttag(self, tag, attrs):
        if tag == 'img':
            pairs = dict(attrs)
            src = pairs['src']
            assert isinstance(src, str), 'Image source is required'
            assert not src.startswith(('http:', 'https:', 'data:')), src
            path = (ROOT / src).resolve()
            assert path.is_relative_to(ROOT), src
            data = base64.b64encode(path.read_bytes()).decode('ascii')
            starttag = self.get_starttag_text()
            assert isinstance(starttag, str)
            literal = starttag.replace(src, f'data:image/png;base64,{data}')
            self.parts.append(literal)
            self.image_count += 1
        else:
            self.parts.append(self.get_starttag_text() or '')
    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
    def handle_endtag(self, tag): self.parts.append(f'</{tag}>')
    def handle_data(self, data): self.parts.append(data)
    def handle_entityref(self, name): self.parts.append(f'&{name};')
    def handle_charref(self, name): self.parts.append(f'&#{name};')


def main():
    text = (ROOT / 'article.md').read_text(encoding='utf-8')
    for path in ROOT.glob('*.md'):
        content = path.read_text(encoding='utf-8')
        assert content.endswith('\n'), f'Missing final newline: {path.name}'
        assert all(line == line.rstrip() for line in content.splitlines()), f'Trailing whitespace: {path.name}'
    assert len(re.findall(r'^```', text, re.M)) % 2 == 0, 'Unbalanced code fences'
    image_refs = re.findall(r'!\[[^\]]*\]\(([^)]+)\)', text)
    manifest = json.loads((ROOT / 'images/image-manifest.json').read_text(encoding='utf-8'))
    assert set(image_refs) == {x['file'] for x in manifest}
    for entry in manifest:
        path = ROOT / entry['file']
        assert hashlib.sha256(path.read_bytes()).hexdigest() == entry['sha256']
        with Image.open(path) as image:
            image.load()
            assert list(image.size) == entry['size']
    rendered = markdown.markdown(text, extensions=['tables', 'fenced_code', 'toc'])
    parser = ImageEmbedder(); parser.feed(rendered)
    assert parser.image_count == len(image_refs)
    css = '''body{font:17px/1.85 -apple-system,BlinkMacSystemFont,"Segoe UI","Microsoft YaHei",sans-serif;color:#222;background:#f5f6f8;margin:0}main{max-width:940px;margin:32px auto;padding:36px 42px;background:white;border-radius:12px}h1{font-size:30px;line-height:1.5}h2{margin-top:44px;border-bottom:1px solid #ddd;padding-bottom:8px}h3{margin-top:28px}img{max-width:100%;height:auto;display:block;margin:20px auto}pre{overflow:auto;max-width:100%;box-sizing:border-box;padding:18px;background:#18212e;color:#e6edf5;border-radius:8px;font-size:14px;line-height:1.65}code{font-family:Consolas,monospace;overflow-wrap:anywhere}p code,li code,td code{background:#eef1f5;padding:2px 4px;border-radius:3px}blockquote{margin:20px 0;padding:10px 18px;background:#eff5ff;border-left:4px solid #547cd6}table{border-collapse:collapse;display:block;overflow:auto;max-width:100%;font-size:15px}td,th{border:1px solid #d9dfe7;padding:8px 12px;text-align:left}a{color:#315fb3;overflow-wrap:anywhere}em{color:#626b78;font-size:14px}@media(max-width:700px){main{margin:0;padding:20px 16px;border-radius:0}h1{font-size:25px}}'''
    html = '<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Herdr 多 Agent 协作：图文审阅稿</title><style>' + css + '</style><main>' + ''.join(parser.parts) + '</main></html>'
    (ROOT / 'article.preview.html').write_text(html, encoding='utf-8')
    # Extract the exact controller instructions, so source and copy cannot drift.
    prompts = re.findall(r'```text\n(.*?)\n```', text, re.S)
    controller = next(x for x in prompts if x.startswith('在当前项目中使用 Herdr'))
    (ROOT / 'code/controller-prompt.txt').write_text(controller + '\n', encoding='utf-8')
    research_files = sorted(p.relative_to(ROOT).as_posix() for p in (ROOT / 'research').iterdir() if p.is_file())
    files = ['article.md', 'article.preview.html', 'references.md', 'publish.md', 'verification.md', 'code/controller-prompt.txt', 'images/image-manifest.json'] + image_refs + research_files
    if (ROOT / 'article.csdn.md').exists():
        final_text = (ROOT / 'article.csdn.md').read_text(encoding='utf-8')
        remote_images = re.findall(r'!\[[^\]]*\]\(([^)]+)\)', final_text)
        assert len(remote_images) == len(image_refs)
        assert all(url.startswith('https://i-blog.csdnimg.cn/') for url in remote_images)
        final_rendered = markdown.markdown(final_text, extensions=['tables', 'fenced_code', 'toc'])
        final_html = html.replace(''.join(parser.parts), final_rendered, 1)
        (ROOT / 'article.csdn.preview.html').write_text(final_html, encoding='utf-8')
        files += ['article.csdn.md', 'article.csdn.preview.html', 'csdn-upload/verified-image-urls.json']
    assert len(files) == len(set(files))
    with zipfile.ZipFile(ROOT / 'review-package.zip', 'w', zipfile.ZIP_DEFLATED) as package:
        for name in files:
            assert (ROOT / name).is_file(), name
            package.write(ROOT / name, arcname=name)
    with zipfile.ZipFile(ROOT / 'review-package.zip') as package:
        assert package.testzip() is None
        assert len(package.namelist()) == len(files)
        assert all(package.read(name) == (ROOT / name).read_bytes() for name in files)
    result = {'image_count':parser.image_count, 'source_characters':len(text), 'han_characters':len(re.findall(r'[\u4e00-\u9fff]',text)), 'markdown_version':markdown.__version__, 'package_file_count':len(files), 'article_sha256':hashlib.sha256((ROOT/'article.md').read_bytes()).hexdigest(), 'preview_sha256':hashlib.sha256((ROOT/'article.preview.html').read_bytes()).hexdigest()}
    print(json.dumps(result, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()

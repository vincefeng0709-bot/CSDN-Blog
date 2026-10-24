"""Prepare an import source using user-uploaded, verified CSDN images.

Reads public images only. Never logs into CSDN, uploads, or publishes.
"""
from concurrent.futures import ThreadPoolExecutor
from io import BytesIO
from pathlib import Path

import hashlib
import json
import re
import requests
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
URLS = [
    'https://i-blog.csdnimg.cn/direct/f16d227819a94823aba7eb4601f90bf7.png#pic_center',
    'https://i-blog.csdnimg.cn/direct/91c6b59d1c1e4300a4911ce72f769e67.png#pic_center',
]

def image_info(data):
    with Image.open(BytesIO(data)) as image:
        image.load()
        rgb = image.convert('RGB')
        return {'sha256':hashlib.sha256(data).hexdigest(), 'rgb_sha256':hashlib.sha256(rgb.tobytes()).hexdigest(), 'size':list(image.size)}

def fetch(url):
    assert re.fullmatch(r'https://i-blog\.csdnimg\.cn/direct/[0-9a-f]{32}\.png#pic_center', url), url
    response = requests.get(url, timeout=60)
    response.raise_for_status()
    return {'url':url, 'resolved_url':response.url, 'status':response.status_code, 'content_type':response.headers.get('Content-Type'), **image_info(response.content)}

def main():
    manifest = json.loads((ROOT/'images/image-manifest.json').read_text(encoding='utf-8'))
    local = {entry['file']:image_info((ROOT/entry['file']).read_bytes()) for entry in manifest}
    with ThreadPoolExecutor(max_workers=2) as pool:
        downloaded = list(pool.map(fetch, URLS))
    assert len(set(URLS)) == len(URLS) == len(local)
    mapping = {}
    for item in downloaded:
        matches = [name for name, info in local.items() if item['size']==info['size'] and item['rgb_sha256']==info['rgb_sha256']]
        assert len(matches)==1, f'Image does not uniquely match local originals: {item}'
        name = matches[0]
        assert name not in mapping
        mapping[name] = item['url']
        item['local_file'] = name
        item['byte_identical'] = item['sha256'] == local[name]['sha256']
    folder = ROOT/'csdn-upload'; folder.mkdir(exist_ok=True)
    (folder/'verified-image-urls.json').write_text(json.dumps(downloaded, ensure_ascii=False, indent=2)+'\n',encoding='utf-8')
    source = (ROOT/'article.md').read_text(encoding='utf-8')
    final = source
    for name, url in mapping.items():
        assert final.count(f']({name})')==1
        final = final.replace(f']({name})',f']({url})')
    refs = re.findall(r'!\[[^\]]*\]\(([^)]+)\)',final)
    assert set(refs)==set(URLS) and len(refs)==2
    assert not any(x.startswith(('images/','file:','data:')) for x in refs)
    restored = final
    for name, url in mapping.items():
        restored = restored.replace(f']({url})',f']({name})')
    assert restored == source, 'Editorial source and CSDN source drifted'
    (ROOT/'article.csdn.md').write_text(final,encoding='utf-8')
    print(json.dumps({'title':source.splitlines()[0][2:],'images':downloaded,'final_file':str(ROOT/'article.csdn.md'),'text_identical_except_image_urls':True},ensure_ascii=False,indent=2))

if __name__=='__main__':
    main()

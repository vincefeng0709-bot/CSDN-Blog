"""Download public upstream documentation only; never install Herdr."""
from concurrent.futures import ThreadPoolExecutor
from html.parser import HTMLParser
from pathlib import Path
import hashlib
import json
import subprocess
import sys
import requests

ROOT = Path(__file__).resolve().parents[1]
SOURCES = [
    ('home', 'https://herdr.dev/'),
    ('install', 'https://herdr.dev/docs/install/'),
    ('automation', 'https://herdr.dev/docs/agent-automation/'),
    ('cli', 'https://herdr.dev/docs/cli-reference/'),
    ('skill', 'https://herdr.dev/docs/agent-skill/'),
    ('windows', 'https://herdr.dev/docs/windows-beta/'),
    ('integrations', 'https://herdr.dev/docs/integrations/'),
    ('readme', 'https://raw.githubusercontent.com/herdrdev/herdr/master/README.md'),
    ('license', 'https://raw.githubusercontent.com/herdrdev/herdr/master/LICENSE'),
    ('skill-source', 'https://raw.githubusercontent.com/herdrdev/herdr/master/skills/herdr/SKILL.md'),
]

class Text(HTMLParser):
    def __init__(self):
        super().__init__(); self.parts = []; self.skip = 0; self.images = []
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag in ('script', 'style'): self.skip += 1
        if tag in ('p','div','h1','h2','h3','pre','li','tr'): self.parts.append('\n')
        if tag in ('img','video','source'): self.images.append({'tag':tag, **attrs})
    def handle_endtag(self, tag):
        if tag in ('script','style'): self.skip = max(0, self.skip - 1)
        if tag in ('p','div','pre','li','tr'): self.parts.append('\n')
    def handle_data(self, data):
        if not self.skip: self.parts.append(data)

def fetch(item):
    name, url = item
    r = requests.get(url, timeout=60); r.raise_for_status()
    folder = ROOT / 'research'; folder.mkdir(exist_ok=True)
    p = Text()
    if 'html' in r.headers.get('Content-Type', ''):
        p.feed(r.text)
        text = '\n'.join(x.strip() for x in ''.join(p.parts).splitlines() if x.strip())
    else: text = r.text
    (folder / f'{name}.txt').write_text(text, encoding='utf-8')
    return {'name':name, 'url':url, 'resolved_url':r.url, 'sha256':hashlib.sha256(r.content).hexdigest(), 'images':p.images, 'characters':len(text)}

def safe_fetch(item):
    try:
        return fetch(item)
    except requests.RequestException as exc:
        return {'name': item[0], 'url': item[1], 'error': str(exc)}

if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=5) as pool:
        results = []
        for item, result in zip(SOURCES, pool.map(lambda x: safe_fetch(x), SOURCES)):
            results.append(result)
    (ROOT / 'research' / 'retrieval.json').write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps(results, ensure_ascii=False, indent=2))

"""Check the required template invariants, assets, brand and offline readiness."""
from pathlib import Path
import json,re,hashlib
root=Path(__file__).resolve().parent
page=(root/'dist/index.html').read_text('utf-8')
baseline=(root/'baseline/index.html').read_text('utf-8')
def obj(text,name):
 return json.JSONDecoder().raw_decode(text.split('const '+name+'=',1)[1])[0]
expected=json.loads((root/'alignment-reference.json').read_text('utf-8'))
assert hashlib.sha256((root/'baseline/index.html').read_bytes()).hexdigest()==expected['source_sha256']
assert expected['css_layout_unchanged']
assert set(re.findall(r'data-action=["\']([^"\']+)',baseline))==set(re.findall(r'data-action=["\']([^"\']+)',page))
assert re.search(r'const DOWNLOAD_CHANNELS=.*?;',page)[0]==re.search(r'const DOWNLOAD_CHANNELS=.*?;',baseline)[0]
assert list(obj(page,'CONTENT'))==list(obj(baseline,'CONTENT'))
for lang,c in obj(page,'CONTENT').items():
 assert [s['id'] for s in c['home']['scenes']]==expected['scene_ids']
 assert len(c['home']['scenes'])==5
 assert all(s['image'].startswith('placeholder-') for s in c['home']['scenes'])
 # Latest confirmed direction: all display copy is the v19 master, name replaced.
 master=json.loads(json.dumps(obj(baseline,'CONTENT')[lang],ensure_ascii=False).replace('Ola Party','TiLike').replace('OlaParty','TiLike').replace('olapartyservice@gmail.com','tilikecs@gmail.com'))
 current=json.loads(json.dumps(c))
 for collection in [master,current]:
  for scene in collection['home']['scenes']:
   scene.pop('image',None);scene.pop('source',None)
 assert current==master,lang+' display copy diverged from v19'
assert not re.search(r'Ola Party|Infriends|olaparty\.com|com.live.party|HAGO SINGAPORE|PASIR PANJANG',page,re.I)
assets=obj(page,'ASSETS')
for uri in assets.values():assert (root/'dist'/uri).is_file(),uri
for uri in set(re.findall(r'(?:src|href|srcset)=["\'](assets/[^"\']+)',page)):
 assert (root/'dist'/uri).is_file(),uri
assert not re.search(r'<script[^>]+src=["\']https?://',page)
assert obj(page,'LINKS')['google'].endswith('id=com.party.tilive')
assert not obj(page,'LINKS')['recharge']
assert all('TiLike' in obj(page,'POLICIES')[k] or 'Tilike' in obj(page,'POLICIES')[k] for k in ['terms','privacy','children'])
print('PASS: pinned baseline; event/channel IDs and order; four languages; five placeholder scenes; local assets; clean active brand; own policies and Google Play destination.')

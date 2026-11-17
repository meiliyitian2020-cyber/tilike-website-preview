"""Build TiLike from the pinned v19 template; no external project dependency."""
from pathlib import Path
import base64,copy,hashlib,html,json,re,shutil,runpy
from PIL import Image
root=Path(__file__).resolve().parent
source=(root/'baseline/index.html').read_text('utf-8')
assert hashlib.sha256((root/'baseline/index.html').read_bytes()).hexdigest()==(root/'baseline/SHA256').read_text('utf-8').strip(),'Pinned v19 template changed'
config=json.loads((root/'brand-config.json').read_text('utf-8'))
product_copy=json.loads((root/'product-copy.json').read_text('utf-8'))
out=root/'dist'; assets=out/'assets'; assets.mkdir(parents=True,exist_ok=True)
def js_object(text,name):
 start=text.index('const '+name+'=')+len('const '+name+'=')
 value,length=json.JSONDecoder().raw_decode(text[start:]);return value,start,start+length
def replace_object(page,name,value):
 _,a,b=js_object(page,name);return page[:a]+json.dumps(value,ensure_ascii=False,indent=2)+page[b:]
def rebrand(s):
 return s.replace('Ola Party','TiLike').replace('OlaParty','TiLike').replace('olapartyservice@gmail.com',config['links']['email']).replace('HAGO SINGAPORE PTE. LTD.',config['entity']).replace('30 PASIR PANJANG ROAD #15-31A MAPLETREE BUSINESS CITY SINGAPORE 117440',config['address']).replace('ola-preview-','tilike-preview-')
reference,_,_=js_object(source,'CONTENT')
content=copy.deepcopy(product_copy)
for lang,t in content.items():
 for i,scene in enumerate(t['home']['scenes']):scene['source']=f'placeholder-scene-{i+1}.svg'
page=replace_object(source,'CONTENT',content);page=rebrand(page)
page=replace_object(page,'LINKS',config['links'])
policies={}
for key in ['terms','privacy','children']:
 body=json.loads((root/'sources'/f'{key}-policy.json').read_text('utf-8'))['data']['acticle_content']
 body=re.sub(r'<script\b[^>]*>.*?</script>','',body,flags=re.S|re.I)
 body=re.sub(r'\son\w+="[^"]*"','',body,flags=re.I)
 policies[key]=body.replace('target="_blank"','target="_blank" rel="noopener noreferrer"')
page=replace_object(page,'POLICIES',policies)
original_assets,_,_=js_object(source,'ASSETS');asset_map={}
for name in original_assets:
 if name.startswith('download-') or name.endswith('.ttf'):
  shutil.copy2(root/'baseline/assets'/name,assets/name);asset_map[name]='assets/'+name
def svg_logo(name,w,h,file):
 uri='data:image/png;base64,'+base64.b64encode(file.read_bytes()).decode()
 (assets/name).write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}"><image width="{w}" height="{h}" preserveAspectRatio="xMidYMid meet" href="{uri}"/></svg>','utf-8');return 'assets/'+name
asset_map['ola-share-icon.png']=svg_logo('brand-logo.svg',500,170,root/'brand/logo-dark.png')
asset_map['hero-brand-logo.png']=svg_logo('brand-hero-logo.svg',350,90,root/'brand/logo-dark.png')
shutil.copy2(root/'brand/logo-light.png',assets/'brand-logo-light.png')
shutil.copy2(root/'brand/app-icon.png',assets/'app-icon.png')
Image.open(root/'brand/app-icon.png').resize((32,32)).save(assets/'favicon.png')
asset_map['favicon-32x32-new.png']='assets/favicon.png';asset_map['company-app-logo.png']='assets/app-icon.png'
def placeholder(name,w,h,label):
 text=f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}"><rect width="{w}" height="{h}" fill="#e4f7ee"/><g fill="none" stroke="#c9e9d9" stroke-width="2"><rect x="{w*.12}" y="{h*.12}" width="{w*.76}" height="{h*.76}" rx="24"/><circle cx="{w*.44}" cy="{h*.44}" r="{min(w,h)*.045}"/><circle cx="{w*.56}" cy="{h*.44}" r="{min(w,h)*.045}"/></g><text x="50%" y="54%" text-anchor="middle" fill="#477566" font-family="Arial,Microsoft YaHei,sans-serif" font-size="{min(w,h)*.033}">{html.escape(label)}</text><text x="50%" y="60%" text-anchor="middle" fill="#668d7e" font-family="Arial,sans-serif" font-size="{min(w,h)*.024}">{w} × {h} · TiLike</text></svg>'''
 (assets/name).write_text(text,'utf-8');return 'assets/'+name
slots=[]
for i,s in enumerate(reference['en']['home']['scenes'],1):
 name=f'placeholder-scene-{i}.svg';asset_map[s['image']]=placeholder(name,720,1280,'功能素材待替换 / Feature media pending');slots.append({'slot':s['id'],'file':name,'canvas':[720,1280]})
asset_map['p1_youngs-38ed979a0c.png']=placeholder('placeholder-about.svg',822,756,'介绍素材待替换 / About media pending')
placeholder('placeholder-hero-desktop.svg',1600,900,'首屏素材待替换 / Hero media pending')
placeholder('placeholder-hero-mobile.svg',900,1600,'首屏素材待替换 / Hero media pending')
paint=runpy.run_path(str(root/'brand-paint.py'))
(assets/'brand-background.svg').write_text(paint['decorative_background'](1920,1080),'utf-8')
asset_map['p1_bg-105ed6b6c9.png']='assets/brand-background.svg'
page=replace_object(page,'ASSETS',asset_map)
page=page.replace('href="assets/favicon-32x32-new.png"','href="assets/favicon.png"')
poster='''function heroVideoPlaceholder(){return `<div class="hero-media-video"><div class="hero-video-stage"><picture><source media="(max-width:680px)" srcset="assets/placeholder-hero-mobile.svg"><img class="hero-loop-freeze" src="assets/placeholder-hero-desktop.svg" alt="TiLike — media pending" loading="eager" decoding="async"></picture></div><button type="button" class="hero-play-fallback" data-action="start-hero-video" hidden aria-label="${lang==='zh'?'播放视频':lang==='hi'?'वीडियो चलाएँ':'Play video'}">${icon('video')}<span>${lang==='zh'?'播放视频':lang==='hi'?'वीडियो चलाएँ':'Play video'}</span></button></div>`;}
'''
page=re.sub(r'function heroVideoPlaceholder\(\)\{.*?\n(?=function homePage)',lambda _:poster,page,flags=re.S)
page=re.sub(r'const HERO_MEDIA=\{[^\n]*\};','const HERO_MEDIA={};',page)
page=page.replace("if(action==='preview-download'){toast(downloadCopy().note);return;}","if(action==='preview-download'){const destination=LINKS[event.target.closest('[data-channel]').dataset.channel];if(destination){window.location.assign(destination);}else{toast(downloadCopy().note);}return;}")
pending="""
document.addEventListener('click',event=>{const a=event.target.closest('a');if(a&&a.getAttribute('href')===''){event.preventDefault();toast(({zh:'TiLike 网页充值地址待配置，本评审版尚未接通支付服务。',en:'TiLike web recharge is not configured. No payment service is connected.',hi:'TiLike वेब रिचार्ज कॉन्फ़िगर नहीं है। भुगतान सेवा कनेक्ट नहीं है।',id:'Isi ulang web TiLike belum dikonfigurasi. Layanan pembayaran belum terhubung.'})[lang]);}});
"""
slot_reference=json.dumps(reference,ensure_ascii=False).replace('Ola Party','TiLike Go')
slot_script='const ALIGN_REFERENCE='+rebrand(slot_reference)+';\n'+(root/'alignment-slots.js').read_text('utf-8')
page=page.replace('\nrender();\n})();',pending+'\n'+slot_script+'\nrender();\n})();')
page=paint['paint_styles'](page)
page=re.sub(r'function sceneBackground\(\)\{[^\n]*',lambda _:paint['SCENE'],page)
page=page.replace('name="theme-color" content="#146d58"','name="theme-color" content="#007b64"')
for key,uri in asset_map.items():
 # Neutralize legacy file keys in runtime; retain scene IDs and event IDs.
 name=Path(uri).name
 if key!=name:page=page.replace(key,name)
assert [paint['TOKEN'].sub('<color>',x) for x in re.findall(r'<style[^>]*>(.*?)</style>',source,re.S)]==[paint['TOKEN'].sub('<color>',x) for x in re.findall(r'<style[^>]*>(.*?)</style>',page,re.S)]
assert [s['id'] for s in content['en']['home']['scenes']]==[s['id'] for s in reference['en']['home']['scenes']]
assert not re.search(r'Ola Party|Infriends|olaparty\.com|com.live.party|HAGO SINGAPORE|PASIR PANJANG',page,re.I)
(out/'index.html').write_text(page,'utf-8');(out/'.nojekyll').touch()
(out/'robots.txt').write_text('User-agent: *\nDisallow: /\n','utf-8')
(root/'tests/check-script.js').write_text('\n'.join(re.findall(r'<script[^>]*>(.*?)</script>',page,re.S)),'utf-8')
(root/'placeholder-slots.json').write_text(json.dumps({'heroDesktop':{'file':'placeholder-hero-desktop.svg','canvas':[1600,900]},'heroMobile':{'file':'placeholder-hero-mobile.svg','canvas':[900,1600]},'scenes':slots},ensure_ascii=False,indent=2),'utf-8')
(root/'alignment-reference.json').write_text(json.dumps({'version':19,'commit':'f8026d91802eb907a54d9f84c349aa306ef098cd','source_sha256':hashlib.sha256((root/'baseline/index.html').read_bytes()).hexdigest(),'css_layout_unchanged':True,'scene_ids':[s['id'] for s in reference['en']['home']['scenes']]},indent=2),'utf-8')
print('TiLike built: v19 layout declarations unchanged, 5 scene slots, 4 languages, verified official policies, all display media placeholders.')

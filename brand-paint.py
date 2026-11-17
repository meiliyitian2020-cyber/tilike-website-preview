"""TiLike paint only: CSS layout declarations are asserted unchanged."""
import re, colorsys
TOKEN=re.compile(r'#[0-9a-fA-F]{3,8}\b|rgba?\([^)]+\)')
EXACT={'#146d58':'#007b64','#d1ff69':'#c5ff58','#ddfaec':'#e0fff0',
 '#fffdf4':'#f5fff9','#19264b':'#202027','#cef5dd':'#d6ffed',
 '#67c99d':'#45dcb0','#ffe476':'#c5ff58','#a4e8bb':'#8cf5c5',
 '#fcfff3':'#f5fff9','#edfbef':'#eafff5','#dcf7e8':'#ddfff0',
 '#dcf4ce':'#daffed','#ffe895':'#dbff95','#72c99d':'#57d5ac',
 '#c9f3e3':'#c5f9e6','#f9e591':'#daff8a','#67c6a5':'#39cda6'}
def brand_color(token):
 low=token.lower()
 if low in EXACT:return EXACT[low]
 if low.startswith('rgb'):
  nums=re.findall(r'[\d.]+',low)
  if len(nums)>=3:
   rgb=tuple(float(n) for n in nums[:3]); alpha=nums[3] if len(nums)>3 else None
   if rgb==(255.,253.,244.): rgb=(245,255,249)
   elif rgb==(25.,38.,75.): rgb=(32,32,39)
   else:
    h,l,s=colorsys.rgb_to_hls(*(n/255 for n in rgb))
    if 35/360<=h<=175/360 and s>.04:rgb=tuple(round(v*255) for v in colorsys.hls_to_rgb(155/360,l,s))
   return ('rgba('+','.join(str(int(n)) for n in rgb)+','+alpha+')') if alpha else 'rgb('+','.join(str(int(n)) for n in rgb)+')'
  return token
 value=low[1:]
 if len(value)==3:value=''.join(c*2 for c in value)
 if len(value) not in (6,8):return token
 rgb=[int(value[i:i+2],16)/255 for i in (0,2,4)];h,l,s=colorsys.rgb_to_hls(*rgb)
 if 35/360<=h<=175/360 and s>.04:
  rgb=colorsys.hls_to_rgb((83 if h<85/360 else 155)/360,l,s)
  return '#'+''.join(f'{round(v*255):02x}' for v in rgb)+value[6:]
 return token
def paint_styles(page):
 return re.sub(r'<style>(.*?)</style>',lambda m:'<style>'+TOKEN.sub(lambda c:brand_color(c[0]),m[1])+'</style>',page,flags=re.S)
def decorative_background(width,height):
 return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 1600 900" preserveAspectRatio="xMidYMid slice"><defs><linearGradient id="base" x2="1" y2="1"><stop stop-color="#e7fff4"/><stop offset="1" stop-color="#f5ffdf"/></linearGradient></defs><rect width="1600" height="900" fill="url(#base)"/><g opacity=".24"><path d="M1250 80h200a75 75 0 0 1 75 75v90a75 75 0 0 1-75 75h-75l-65 60 12-60h-72a75 75 0 0 1-75-75v-90a75 75 0 0 1 75-75Z" fill="#8ef2bc"/><g fill="none" stroke="#47cfa2" stroke-width="8"><path d="M80 680a80 80 0 0 1 160 0M280 680a80 80 0 0 1 160 0"/></g><circle cx="1440" cy="640" r="24" fill="#b3ed53"/><circle cx="1100" cy="180" r="8" fill="#00b88d"/><circle cx="170" cy="140" r="12" fill="#a1eb78"/></g></svg>'''
SCENE='''function sceneBackground(){return `<div class="scene-backdrop" aria-hidden="true"><i></i><svg viewBox="0 0 720 420" fill="none"><path d="M430 50h180a45 45 0 0 1 45 45v100a45 45 0 0 1-45 45h-70l-50 48 9-48h-69a45 45 0 0 1-45-45V95a45 45 0 0 1 45-45Z" fill="var(--scene-lime)"/><g stroke="var(--scene-line)" stroke-width="5"><path d="M90 320a60 60 0 0 1 120 0M245 320a60 60 0 0 1 120 0"/></g><circle cx="610" cy="340" r="20" fill="var(--scene-yellow)"/><circle cx="350" cy="100" r="9" fill="var(--scene-line)"/></svg></div>`;}'''

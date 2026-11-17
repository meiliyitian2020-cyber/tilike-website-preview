from pathlib import Path
import zipfile
root=Path(__file__).resolve().parent
target=root/'TiLike-offline-review.zip'
with zipfile.ZipFile(target,'w',zipfile.ZIP_DEFLATED) as z:
 for file in (root/'dist').rglob('*'):
  if file.is_file():z.write(file,file.relative_to(root/'dist'))
 z.writestr('打开说明.txt','解压后双击 index.html。页面、字体、标识和占位图均在包内。Google Play 和官方协议外链需联网。\n所有未确认下载渠道、充值和表单后台均有清楚的未接通反馈。')
print(target)

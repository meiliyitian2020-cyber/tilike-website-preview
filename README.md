# TiLike 官网独立评审版

继承 Ola 已确认第 19 版（`f8026d91802eb907a54d9f84c349aa306ef098cd`）结构与交互。按 2026-11-17 最新确认：所有展示文案、标题全部复用母版，仅替换产品名、真实标识、事实信息、品牌绘制和占位展示素材；原 Ola、Infriends 项目与共享盘物料未修改。

## 本地使用

```powershell
pip install -r requirements.txt
python build-aligned.py
python verify.py
node --check tests/check-script.js
python -m http.server 4318 --directory dist
```

访问 `http://127.0.0.1:4318/?lang=zh`。也可直接打开 `dist/index.html`。`python package-offline.py` 生成独立离线包，解压后打开 `index.html`。

## 可修改配置

- `brand-config.json`：本产品主体、地址、邮箱、目的链接、品牌色参考。
- `product-copy.json`：四种语言的全部展示文案，逐项复制 Ola 第 19 版，只替换产品名及邮箱。`verify.py` 强制验证与母版一致。
- `brand-paint.py`：实际使用的全站颜色映射及非布局装饰。
- `placeholder-slots.json`：首屏及五场景资源槽位。首屏桌面 1600×900、手机 900×1600，场景 720×1280。
- `brand/`：真实横版深浅 Logo、经官方页面核验的 icon。保持等比，未重画品牌。
- `sources/*-policy.json`：从 TiLike 官方页面所用公开 API 读取的正式协议原文。正文保留英文及原有拼写。
- `alignment-slots.js`：以母版原文槽位预留高度，控制翻译和事实信息长度，不改 CSS 功能盒子。隐藏测量文字中的 TiLike Go 只是母版宽度测量文本，不是产品名称，也不会呈现在页面中。

`baseline/` 是本项目内自包含的第 19 版审计母版与通用徽章/字体，原品牌只在该只读参考和来源快照中存在，不部署到评审网站。运行构建无需访问其他产品目录或共享盘。

## 功能边界

保留全部路由、场景 ID（`voice/live/pk/games/creator`）、`data-action/data-channel/data-slide` 与渠道顺序。功能标题、说明和导航文字同样按最新确认直接复用母版，不再应用此前的产品能力提炼文案。

Google Play 为已核实渠道；其余下载地址及网页充值未知，入口原位保留并反馈。表单只校验，不发送；Cookie 偏好保存在当前浏览器；无生产统计上报。正式缺失项及事实差异见 `SOURCES-AND-PENDING.md`。

## 发布

使用本产品独立 GitHub 仓库的 `main` 分支，GitHub Actions 重新构建和检查后仅发布 `dist/` 至 GitHub Pages。仓库、网址与提交记录见 `DEPLOYMENT.md`。没有沿用其他产品的托管 ID、域名或 Git 元数据。

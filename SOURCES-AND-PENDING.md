# 来源、事实差异与待确认项

来源采集：2026-11-13；交付验证：2026-11-17。

**最新确认口径（2026-11-17）**：用户明确要求所有展示文案与标题完整复用 Ola 第 19 版，仅替换产品名、标识、配色、装饰及主体/地址/邮箱/链接等事实信息。此确认覆盖最初“按 TiLike 能力重新提炼场景文案”的要求。最终 `product-copy.json` 与母版逐字段比对，产品名和邮箱除外完全一致。三份正式协议仍使用 TiLike 官方正文，事实资料不使用其他产品内容。

## 产品身份和事实来源

| 项目 | 来源与采用内容 |
|---|---|
| 飞书原官网 | [原官网链接表](https://lp3jrqympq.feishu.cn/wiki/X4Czwro8ci1QBikh3uRccNDMnsb?sheet=ymlzGV) 的 TILIKE 列为 `tilike.net`，已通过登录浏览器目视核对 |
| 官网 | [TiLike](https://tilike.net/) 返回 200，进入 `#/home`，显示 TiLike；官方 JS 引用 `static.tilive.net` |
| Slogan | 官网：Connect with Friends, Live Your Life. |
| 产品能力 | [Google Play 官方页](https://play.google.com/store/apps/details?id=com.party.tilive&hl=en)：TiLike；开发者 CHIVALYOUTH TECHNOLOGY PTE. LTD.；包名 `com.party.tilive`；语音聊天室、直播、与主播及房间成员讨论互动。此为资料核对记录；最终五槽位文案按用户最新确认直接复用 Ola，不再使用这些资料重写 |
| About | 官网 `#/about`：新加坡科技公司创立，持续探索交互体验，致力于温暖、多元、友爱、包容的社交空间。此为原官网资料记录；最终 About 展示文案按最新确认复用母版，仅替换产品名 |
| 主体 | 官网页脚：Chivalyouth Technology PTE.LTD.；主页采用该原文 |
| 地址 | 官网页脚：65 CHULIA STREET# 38-02 / 03 OCBC CENTRE SINGAPORE (049513) |
| 支持邮箱 | 官网 About 和商店支持邮箱：tilikecs@gmail.com |
| 标识 | 共享盘完整 Logo 与官网横版标识一致；共享盘 `Tilive 1024@1x.png` 图形与完整 TiLike Logo、官网 favicon 一致，经核验后复制为 `brand/app-icon.png`。未以文件名判定为其他品牌 |

官网原始 HTML/JS、官方横版 Logo/favicon、商店页面、三份协议响应均保留在 `sources/`，不参与首页展示。

## 正式协议

- [Terms of Service](https://www.tilike.net/a/license/tilike-user.html?lang=en)
- [Privacy Policy](https://www.tilike.net/a/license/tilike-privacy.html?lang=en)
- [Safety Policy for Children](https://www.tilike.net/a/license/children-policy.html)

这些官方页面的加载脚本使用 `https://feapi.tilike.net/post-platform/getPostDetail?lang=en`。按其公开请求头 `x-app-name: tilive`、`x-app-post-type: user/privacy/children-policy` 读取正文。前两份 `x-app-os: android`，儿童政策 `web`。原文嵌入母版既有三个正式政策页；原官方链接仍可打开。仅移除脚本和事件属性等可执行内容，正文未替换品牌。

## 来源差异（保留，未擅自统一）

1. 官网主体为 `Chivalyouth Technology PTE.LTD.`；商店/条款为 `CHIVALYOUTH TECHNOLOGY PTE. LTD.`；隐私政策正文为 `Chivalyouth Technoloy Pte. Ltd.`，其中 Technoloy 拼写不同。页脚使用官网版本；政策保留官方原文，待主体确认。
2. 商店描述的 Website 使用 `https://www.tilive.net`，官网与协议主要使用 `tilike.net`，包名仍为 `com.party.tilive`。均为经官方交叉链接核对的技术历史命名，未改写为猜测地址。
3. 商店开发者联系信息还出现 `contact@trumeet.net`，与 TiLike 支持邮箱不同。页面只使用官网及商店共同确认的 `tilikecs@gmail.com`，开发者联系邮箱差异待业务确认。
4. 儿童安全政策有专用举报邮箱 `tilikechildreport@gmail.com`；保留在该官方政策正文，不替换为通用客服邮箱。
5. 隐私政策显示 2024 年更新日期，儿童政策为 December 2024；不伪造更新日期。官网 meta 曾写 Watch the live and have a party，当前可见主 slogan 采用官网正文版本。

## 飞书缺失项映射和接入状态

已通过当前登录浏览器核对同文件“官网缺失项”表。保持母版模块数量与顺序，不添加画廊或后台页面。

| 缺失分类 | 本次落实 | 仍待提供/接入 |
|---|---|---|
| 下载与页面导航 | 七渠道原位保留；更多渠道弹层；四语导航、About、Help、Contact | App Store、APK、小米、OPPO、vivo、华为官方地址；目前逐项清楚反馈未知 |
| 支付能力 | 充值入口原位保留并提示未配置 | 本产品充值 URL、支付服务商、后端、订单查询与安全测试；没有接通或模拟支付 |
| 用户支持 | FAQ 搜索、分类、账号/封禁/充值/举报/下载指导；正确客服 mailto；表单前端校验 | 工单/邮件发送后台、客服流程与时效。FAQ 为一般求助指引，不保证恢复、退款或处理时间 |
| 合规与安全 | 三份产品正式协议原文；安全中心；社区、反欺凌、Cookie、执法请求入口 | 后四项正式正文和流程。现有页面明确为待确认提纲，不冒充正式政策 |
| 多语言支持 | 母版 English、Indonesia、हिन्दी、中文完整切换；文案槽位对齐 | 产品与法律翻译终审；正式协议目前保留英文并提示来源 |
| 产品介绍 | 首屏与五个功能场景、About；所有展示文字按 2026-11-17 最新确认复用 Ola 第 19 版 | 最终宣传文字及所有展示素材。当前所有首页图、视频/人物/截图均为占位，没有生成宣传图或视频 |
| 运营数据统计 | 既有 `data-action/data-channel/data-slide`、路由、场景 ID 与顺序保留 | 国家/地区、DAU、支付事件、生产埋点接收端与同意策略；未伪造上报或数据 |

Cookie 控制仅保存浏览器偏好，无分析或广告追踪服务。建议正式上线前逐项完成以上业务接入与法务核定。

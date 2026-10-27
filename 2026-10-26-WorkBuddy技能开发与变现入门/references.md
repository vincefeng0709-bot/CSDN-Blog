# 参考资料与核查说明

访问日期：2026-10-26（中国标准时间）。主要来源为腾讯云 / WorkBuddy 官方国内站，不用转载文章或视频的收益口径替代平台规则。

本文件与正文共享本地来源台账 `research/citations.json` 中的编号；该台账与内部核查材料只在本地保存，不纳入公开归档。编号不连续是保留来源身份的结果，不是缺页。完整公开链接由台账生成，见文末 Sources。

## 来源与结论对应关系

| 编号 | 原始资料 | 机构 | 支持的结论与适用边界 |
| --- | --- | --- | --- |
| [1] | 收入变现 | WorkBuddy 开放平台 | 技能和专家的两种付费模式、开通资料审核与微信签约、收入管理；FAQ 明示仍在内测及暂不支持转付费。公开流程不证明某账号已获资格。 |
| [2] | 技能 | WorkBuddy 开放平台 | SKILL.md、YAML frontmatter、必填字段、可选子目录、参考文件引用与 ZIP 解析排查。以读取时的正文为准，不沿用旧搜索摘要。 |
| [3] | WorkBuddy 开放平台开发者公约（试行） | WorkBuddy 开放平台 | 版本 1.0，页面日期 2026-10-22。功能披露、测试、收费与额外费用、重复铺量、知识产权、权限与数据边界。不是独立法律意见。 |
| [4] | 技能（客户端功能文档） | WorkBuddy | 创建与导入入口、安装与启用、关闭后的会话行为、积分与数据风险。页面显示最后更新 2026-10-16 15:10:41。未验证本机客户端界面。 |
| [5] | 开放平台概述 | WorkBuddy 开放平台 | 入驻、认证、创建资产、提交审核、发布、维护的总体顺序。未登录后台执行。 |
| [7] | 服务类目（个人主体） | WorkBuddy 开放平台 | 个人主体的工具/办公等服务类目及对应范围。不能保证本例审核通过。 |
| [8] | 运营数据 | WorkBuddy 开放平台 | 安装与调用为次数、不去重；技能读取文件计为调用；T+1 更新。不可把次数当独立客户或收入。 |
| [9] | 入驻开放平台 | WorkBuddy 开放平台 | 当前个人认证证件范围、手机号邮箱与人脸核验准备、个人主体限制。用户本人操作。 |
| [10] | 实践八：自我进化—创建自己的Skills（技能） | WorkBuddy | 自然语言描述能力、触发方式与输出，创建可复用技能。页面显示最后更新 2026-07-08 10:45:39。 |
| [11] | 腾讯云WorkBuddy开放平台开发者服务协议 | 腾讯云 | 发布及生效日期 2026-08-31；第 3.6 条不承诺流量，第 10 条将费率、结算和提现规则指向公示，并涉及支付机构、税费和退款安排。没有本次账号的具体费率。 |

## 证据与不确定性

- `research/retrieval.json` 保存各已读页面的标题、原始 URL、读取时间、正文 SHA-256 和短摘录。摘录由程序检查逐字存在于实际读取文本中。
- `research/claim-evidence.json` 补充技能规范的必要字段表，以及付费内测、转付费限制、协议条款的关键证据；各行均与已读正文精确匹配。HTML 审核预览将台账生成的来源 URL 转为可点击链接，Markdown 保留台账生成的 Sources 原文。
- 正文事实来源于公开网页读取，不只依据搜索摘要；不附整份服务协议全文，避免不必要转载。
- 未获得当前账号的变现入口、签约条款、费率、包体限制、审核进度或账单。因此正文不补造这些参数。
- 官方付费防复制说明仅按平台主张表述，没有独立验证加密或安全效果。
- 搜索服务返回过与当前字段表不一致的旧摘要，正文采用当前浏览器读取的完整字段表。
- 通用引用工具将中文短句按空白分词判为少于 3 个词，拒绝录入证据；没有给原文插入空格绕过。短摘录改用本地精确子串匹配留证，常规引用编号检查仍单独执行，不声称通过该工具的 evidence gate。

## 视频与截图素材边界

用户提供的 YouTube 截图显示 WorkBuddy 开放平台首页和“AI Skill 也能卖钱”相关标题，但没有可核验的视频 URL 或完整字幕。本文没有冒充观看过完整视频，没有推断博主身份、发布时间、实际收入或账户审核结果，也没有把搜索到的另一条视频当成同一素材。

视频截图只作选题线索，未复制进正文，也未将博主头像或视频画面用作封面。

正文图片为本次读取的公开官方 FAQ 截图，出处为来源 [1]；仅说明内测与规则，不代表商户后台或实操收益。图片详情与校验值见 `images/image-manifest.json`。

## Sources

[1] https://open.workbuddy.cn/docs/monetization — 收入变现
[2] https://open.workbuddy.cn/docs/skill — 技能
[3] https://open.workbuddy.cn/docs/developer-agreement — WorkBuddy 开放平台开发者公约（试行）
[4] https://www.workbuddy.cn/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Skills-Market — 技能｜WorkBuddy 客户端文档
[5] https://open.workbuddy.cn/docs — 开放平台概述
[7] https://open.workbuddy.cn/docs/service-categories-individual — 服务类目（个人主体）
[8] https://open.workbuddy.cn/docs/operations-data — 运营数据
[9] https://open.workbuddy.cn/docs/onboarding — 入驻开放平台
[10] https://www.workbuddy.cn/docs/workbuddy/From-Beginner-to-Expert-Guide/Practice-Cases/Practice-Eight — 实践八：自我进化—创建自己的Skills（技能）
[11] https://rule.tencent.com/rule/202608300002 — 腾讯云WorkBuddy开放平台开发者服务协议

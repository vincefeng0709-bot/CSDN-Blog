# 发布准备

## 状态

**已发布 / 2026-11-11**（发布 URL 与时间经 RSS 核实；此前浏览器自动发布受阻——Chrome 后台进程反复占用配置文件锁，改为用户手动上传完成发布）

## 手动上传交付（2026-11-11）

- 平台专用稿：`article.csdn.md`（正文与 article.md 一致；已移除草稿标记和本地链接；7 个图片位置为【图片N：文件名 —— 内容】占位标记，上传图片后需替换）
- 图片目录：`images/`（7 张，按图片1~7 顺序对应占位标记）
- 待办：用户在 CSDN 编辑器手动上传图片并替换占位标记；若用户提供上传后的图片 URL，可回填生成最终导入版并记录到本文件

## 图片 URL 映射（2026-11-11 已验证）

用户上传后提供 7 个 URL；按内容逐一比对（MD5 与本地原图完全一致），**上传返回顺序与正文位置不一致**，已按内容匹配后写入 `article.csdn.md`。注意：URL 必须逐字符完整使用，截断哈希会被 CDN 返回占位图。

| 图 | 本地文件 | CSDN URL（direct/ 后的哈希） |
| --- | --- | --- |
| 1 | 01-enable-developer-mode.png | 0519a550993d4f7e9d849def5e51775c |
| 2 | 02-configure-third-party-inference.png | c306818718f0427a9fa4097d8c0c6e22 |
| 3 | 03-new-configuration.png | 527474379f4e492fbe011dce3eb661a8 |
| 4 | 04-credential-static-api-key.png | b405343b11b047c1ac83632644648186 |
| 5 | 05-deepseek-anthropic-base-url.png | 2ff78232496f430188f2301d65b4d402 |
| 6 | 06-cowork-model-picker.png | f5b8e41496ac47c98bd139786324083e |
| 7 | 07-local-cowork-deepseek-verified.png | 55ff00f1fce446e38b35213dc82fd610 |

验证：7/7 线上图片 HTTP 200 且与本地原图逐字节一致；正文中按 01→07 顺序出现；`#pic_center` 与描述性 alt 文本保留。

## 状态更新

**已发布（2026-11-11）**，发布 URL 与时间已经 RSS 元数据核实：

- URL（用户提供，含spm参数）：`https://blog.csdn.net/m0_66081030/article/details/170517939?spm=1001.2014.3001.5501`
- 无参阅读 URL：`https://blog.csdn.net/m0_66081030/article/details/170517939`
- 发布时间（RSS pubDate）：2026-11-11 12:29:51 +0800
- 线上标题（RSS 实测）：带书名号《》，比确认标题多一对引号，需用户确认是否有意
- 核实方式与局限：账号 RSS（`/rss/list`）确认标题、链接、发布时间；文章正文页面对本会话浏览器返回 403（CSDN 反爬），正文与图片在页面中的最终显示效果由用户本人确认；7 张图片的 CDN 可用性此前已独立验证（HTTP 200、与本地原图逐字节一致）

## 最终版本（2026-11-11 用户确认）

- **发布标题**：不用第三方工具：Claude 桌面端官方网关直连 DeepSeek 与 Kimi
- **摘要**：Claude 桌面端内置的 Configure Third-Party Inference（第三方推理配置）可以直接把推理请求指向 Anthropic 协议兼容端点。本文以 DeepSeek 为主线实测全流程：开启开发者模式 → 新建配置 → 填 Anthropic 兼容 base URL → 选 Static API key → Apply Changes，并给出 Kimi 的对应配置。全程无需第三方代理工具。
- **标签**：Claude、DeepSeek、Kimi、API、开发者模式、大模型
- **分类**：AI / 大模型开发（以 CSDN 发布时可选列表为准）
- 摘要、标签、分类已经用户确认；发布操作尚未授权。

## 候选标题

1. 手把手教你用官方开发者模式，把 DeepSeek / Kimi 接入 Claude 桌面端
2. 不用第三方工具：Claude 桌面端官方网关直连 DeepSeek 与 Kimi
3. Claude 桌面端换引擎：官方开发者模式接入 DeepSeek / Kimi 实测

## 摘要

Claude 桌面端内置的 Configure Third-Party Inference（第三方推理配置）可以直接把推理请求指向 Anthropic 协议兼容端点。本文以 DeepSeek 为主线实测全流程：开启开发者模式 → 新建配置 → 填 Anthropic 兼容 base URL → 选 Static API key → Apply Changes，并给出 Kimi 的对应配置。全程无需第三方代理工具。

## 标签

Claude、DeepSeek、Kimi、API、开发者模式、大模型、MCP/接入

## 分类

AI / 大模型开发

## 发布前检查项

- [x] 技术结论有依据（视频截图 + DeepSeek/Kimi 官方文档，见 references.md）
- [x] DeepSeek 部分为本机实测，curl 命令标注为示例
- [x] 图片为视频截图 + 作者本机实测截图（07），无 API Key；07 截图左下角用户名"Maoxiny"及任务名称，用户已于 2026-11-11 确认直接使用现状
- [x] 模型名、base URL 与 2026-11-11 查询的官方文档一致，时效性提示已写入正文；已补充说明界面模型命名差异（deepseek-v4-pro vs deepseekv4-pro）
- [x] Kimi 部分按用户意见处理：一句话带过并附官方文档链接，不在正文强调验证状态
- [ ] Claude Desktop 版本号：用户确认为撰写时最新版，具体版本号未记录（references.md 已如实注明）
- [ ] 用户确认最终版本后方可发布

# 参考资料

以下资料均为撰写本文时实际查阅过的来源，查阅日期：2026-11-11。

1. **视频：《🐴 手把手教你Claude桌面版，官方渠道接入国产ai大模型，安全又可靠，无需第三方工具》**
   - 链接：https://www.youtube.com/watch?v=GOtwq2F1bgI
   - 用途：本文整体操作流程（开启开发者模式 → Configure Third-Party Inference → 新建配置 → Static API key → Apply Changes）的演示依据；文中截图 01、02、03、04、06 取自该视频画面。
   - 备注：视频未提供公开字幕，流程细节以用户提供的视频截图为准。

2. **DeepSeek API 文档：首次调用 API**
   - 链接：https://api-docs.deepseek.com/zh-cn/ （"首次调用 API"页面）
   - 支持结论：DeepSeek 提供 Anthropic 兼容 base_url `https://api.deepseek.com/anthropic`；当前模型为 `deepseek-v4-flash` / `deepseek-v4-pro`，`deepseek-chat` 与 `deepseek-reasoner` 将于北京时间 2026-07-24 23:59 弃用。
   - 文中截图 05 取自该页面。

3. **Kimi 开放平台文档：API 概述**
   - 链接：https://platform.kimi.com/docs/api/overview
   - 支持结论：Kimi API 兼容 Anthropic Messages 协议，base_url 为 `https://api.moonshot.cn/anthropic`，接口路径 `/anthropic/v1/messages`；鉴权使用 `Authorization: Bearer $MOONSHOT_API_KEY`。

4. **Kimi 开放平台文档：在 Claude Code 中使用 Kimi**
   - 链接：https://platform.kimi.com/docs/guide/claude-code-kimi
   - 支持结论：Kimi 模型名（如 `kimi-k3[1m]`、`kimi-k3.1-pro`、`kimi-k2.7-code`、`kimi-k2.6`）；国内站与国际站 Key 不通用、base URL 须与创建 Key 的平台一致；curl 验证端点与 Key 的方法。

## 本地实验记录

- DeepSeek 接入：作者在 Windows 11 本机 Claude Desktop（Cowork 界面）按文中流程配置，模型选择器出现 DeepSeek 模型（本机显示为 `deepseek-v4-pro`），对话正常返回；本机 Cowork 主界面截图存于 `images/07-local-cowork-deepseek-verified.png`。实测人：作者本人（用户），Claude Desktop 具体版本号未记录（用户确认撰写时为最新版）。
- Kimi 接入：未实测，状态为待验证。

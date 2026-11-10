# 发布准备

## 状态

**本地草稿 / 未发布**

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

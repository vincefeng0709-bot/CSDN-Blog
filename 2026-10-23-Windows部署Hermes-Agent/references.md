# 参考资料与结论映射

访问日期：2026-10-23（本地 UTC+08:00）。以下为本次实际打开的官方资料，不以搜索摘要代替正文。仅概括相关结论，不复制大段原文。

修订说明：文章已改为 Windows 安装、智谱国内 GLM 接入与新闻 HTML 实战。当前正文使用 R01—R04、R11—R14；R05—R10 保留为最初规划查阅记录，不据此扩展正文范围。资料核查与用户已有操作分别记录，不冒充本轮重新部署。

版本边界：在线文档会更新，未证明页面内容与本地 `v0.22.4` 检出逐项相同。产品能力须与当前安装再核对；文档中的演示模型不是本机已接入模型。URL 以代码形式保留，供后续发布审校使用。

## R01 — Installation

- 机构：Nous Research / Hermes Agent。
- URL：`https://hermes-agent.nousresearch.com/docs/getting-started/installation`
- 实际查阅：Desktop 包、命令行安装与源码安装说明。
- 支持结论：官方区分安装方式；不能把源码安装和打包 Desktop 的步骤混为一次实际经历。
- 本地限制：用户补充了官网下载与 INSTALL 安装入口截图；未记录完整中间过程和安装包文件名，本轮未执行安装。正文区分该画面与当前预打包 Desktop 安装方式。

## R02 — Windows (Native) Guide

- 机构：Nous Research / Hermes Agent。
- URL：`https://hermes-agent.nousresearch.com/docs/user-guide/windows-native`
- 实际查阅：Windows 原生安装、路径参数、How Hermes runs shell commands on Windows。
- 支持结论：官方有 Windows 原生使用路线；终端工具通过 Git Bash 执行命令。PowerShell 应明确作为被调用程序。
- 本地对应：当前 Shell 与 PowerShell 调用已有真实输出，但不代替安装复现。

## R03 — Profiles: Running Multiple Agents

- 机构：Nous Research / Hermes Agent。
- URL：`https://hermes-agent.nousresearch.com/docs/user-guide/profiles`
- 实际查阅：What are profiles、Profiles, agents, and bots。
- 支持结论：Profile 是配置与持久数据的归属目录；它不是文章工作目录。
- 本地对应：`csnd-blog` 的 HERMES_HOME 与会话记录一致；未验证所有隔离机制。

## R04 — Hermes Agent Configuration

- 机构：Nous Research / Hermes Agent。
- URL：`https://hermes-agent.nousresearch.com/docs/user-guide/configuration`
- 实际查阅：配置管理入口、配置文件职责与 reasoning_effort 相关说明。
- 支持结论：推理强度属于需区分适用对象的配置；存在设置机制，不代表本次实际值已确定。
- 本地限制：写作会话的实际推理强度仍未确认；用户新增的 GLM 配置截图显示 medium，任务截图显示 High。它们是不同会话或状态的证据，不混写为同一实际请求参数。

## R05 — Configuring Models

- 机构：Nous Research / Hermes Agent。
- URL：`https://hermes-agent.nousresearch.com/docs/user-guide/configuring-models`
- 实际查阅：模型配置、辅助模型与变更后会话行为的说明。
- 支持结论：主模型、专用辅助模型与运行中会话状态应分开讨论；辅助模型不等同于任意委派子任务。
- 本地限制：没有切换或测试辅助模型，也没有重新执行接入流程。

## R06 — Context Files

- 机构：Nous Research / Hermes Agent。
- URL：`https://hermes-agent.nousresearch.com/docs/user-guide/features/context-files`
- 实际查阅：Supported Context Files、AGENTS.md 与目录链说明。
- 支持结论：Hermes 支持项目上下文文件；AGENTS.md 属于该机制。
- 边界：本文不穷举发现优先级；IDEA.md 的读取是本项目规则，不宣称为内置自动发现。上下文规则不是操作系统权限隔离。

## R07 — Subagent Delegation

- 机构：Nous Research / Hermes Agent。
- URL：`https://hermes-agent.nousresearch.com/docs/user-guide/features/delegation`
- 实际查阅：委派说明、Model Override、Cost strategy、Delegation strategies。
- 支持结论：`delegation.model` 与 `delegation.provider` 支持子模型覆盖；模型覆盖省略时继承父模型。默认策略不等于逐任务任意选模型；高级策略另有机制。
- 本地限制：未运行低成本子模型，不引用文档中的成本概括作为本机实测数据。

## R08 — Mixture of Agents

- 机构：Nous Research / Hermes Agent。
- URL：`https://hermes-agent.nousresearch.com/docs/user-guide/features/mixture-of-agents`
- 实际查阅：页面定义、参考模型与聚合模型的分工。
- 支持结论：参考模型提供分析，聚合模型负责响应与工具调用；它与本文拟议的标准化子任务流水线不同。
- 本地限制：未配置或运行 MoA，不给出成本结论。

## R09 — Get-Location

- 机构：Microsoft Learn。
- URL：`https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-location?view=powershell-7.5`
- 实际查阅：Description、基础示例；页面正文可读取，虽带有授权提示。
- 支持结论：Get-Location 返回当前工作位置相关对象。
- 版本限制：所读页面为 PowerShell 7.5，本机实测为 Windows PowerShell 5.1；不将该页面当作本机版本的完整兼容性证明。

## R10 — Git: git-status Documentation

- 机构：Git 项目。
- URL：`https://git-scm.com/docs/git-status`
- 实际查阅：DESCRIPTION、--short 与 --porcelain 选项。
- 支持结论：git status 检查工作区、暂存区和未跟踪文件；不证明远程推送或 CSDN 发布。
- 本地对应：创建文章前 `git status --short` 无输出。

## R11 — 智谱快速开始

- 机构：智谱 AI / BigModel。
- URL：`https://docs.bigmodel.cn/cn/guide/start/quick-start`
- 实际查阅：注册登录、获取 API Key、产品类型区分和 HTTP 请求示例。
- 支持结论：标准 API 与套餐密钥分开管理；国内 HTTP 请求示例使用 `https://open.bigmodel.cn/api/paas/v4/chat/completions`，基础地址与完整调用地址应区分。
- 本地对应：用户选择普通国内 API；配置截图选择 China 端点。未读取真实 Key，未查询账号余额。

## R12 — GLM-5.3-Flash/FlashX

- 机构：智谱 AI / BigModel。
- URL：`https://docs.bigmodel.cn/cn/guide/models/vlm/glm-5.3-flash.md`
- 实际查阅：如何使用、模型代码、能力支持与思考参数说明。
- 支持结论：文档列出 `glm-5.3-flash` 模型代码和 Function Calling 支持；不同模型的思考参数并非任意互换。
- 使用边界：不转述榜单、营销对比、速度或价格数字；客户端保存 medium 不等于已经抓取并核对服务端实际参数。

## R13 — Hermes Desktop

- 机构：Nous Research / Hermes Agent。
- URL：`https://hermes-agent.nousresearch.com/docs/user-guide/desktop`
- 实际查阅：Which interface is which、Desktop 与 CLI 的核心及配置共用说明。
- 支持结论：Desktop 是同一 Agent 核心的界面；同环境同 Profile 时可从 CLI 配置再回 Desktop 使用，不等于任意远程后端或 Profile 自动同步。
- 查询记录：起初猜测 `/user-guide/hermes-desktop` 返回 404，随后通过官方 `llms.txt` 定位正确页面；失败 URL 不列为参考文献。

## R14 — Tools & Toolsets

- 机构：Nous Research / Hermes Agent。
- URL：`https://hermes-agent.nousresearch.com/docs/user-guide/features/tools`
- 实际查阅：工具分类、搜索与文件工具、Tool Gateway 和 `hermes tools` 入口。
- 支持结论：搜索和文件操作由工具提供；工具的启用及服务权限与主模型接入不同。不能保证国内 GLM Key 自动包含搜索工具服务。
- 本地对应：历史会话有搜索及写入记录，不复制搜索服务凭据；本文未重配搜索服务。

## 本地事实来源（不是外部参考文献）

- 项目根目录 AGENTS.md、IDEA.md。
- 当前 Profile 的安全配置字段、环境变量与只读会话元数据。
- 规划阶段和创建阶段的真实终端工具结果。
- 当前 Profile 中历史 PowerShell 调用的原始工具消息。
- 用户提供的 16 张原始图片，以及 `images/image-manifest.json` 中记录的 15 张裁剪或脱敏副本。
- default Profile 的相关历史会话：模型记录 `glm-5.3-flash`、四次搜索原始工具返回、HTML 写入原始返回。只读核查相关记录，未修改该 Profile。
- 桌面原始 HTML 与 `code/ai-news-report.original.html` 的逐字节一致归档；新闻内容不作为已经核实的外部依据。

具体映射、图片处理清单与失败尝试保留在本机的内部核查记录，本次公开 GitHub 归档不包含这些记录或原图。不公开复制完整 Profile、认证文件或全部会话。归档后的主要阅读入口见 [README.md](README.md)。

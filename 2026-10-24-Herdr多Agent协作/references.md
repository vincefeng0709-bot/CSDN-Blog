# 资料与插图来源

访问日期：2026-10-24（本机日期已通过命令核实）。机构：Herdr 项目维护者。正文引用编号由 `research/citations.json` 管理，文末 Sources 由引用工具生成。

## 已查阅资料及支持结论

| 正文编号 | 资料 | 支持内容 | 本地读取副本 |
| --- | --- | --- | --- |
| 1 | Herdr 官网 | 产品定位；主页展示含交互式演示，不能当作真实实验记录 | `research/home.txt` |
| 2 | Install Herdr | Windows、Linux、macOS 安装；Windows 包含 ConPTY 运行时；stable 通道 | `research/install.txt` |
| 3 | Agent automation | 面板与 Agent 区别；启动、派工、状态、等待、读取与超时语义 | `research/automation.txt` |
| 4 | CLI reference | 参数、JSON 返回字段、工作树命令、错误与输出格式 | `research/cli.txt` |
| 5 | Agent skill file | Skill 安装、全局与项目范围、HERDR_ENV、二进制附带 Skill | `research/skill.txt` |
| 6 | Windows support | 原生支持、ConPTY、IME/剪贴板/附着与 handoff 限制 | `research/windows.txt` |
| 7 | Integrations | 配置修改范围；Claude/Codex 状态检测与 OpenCode 主动报告的区别 | `research/integrations.txt` |
| 8 | 官方仓库 README | 不替换 Agent；后台保持运行与重启恢复的区别 | `research/readme.txt` |
| 9 | 官方仓库 LICENSE | 仓库 Apache-2.0 许可文本 | `research/license.txt` |
| 10 | 官方仓库 Skill 源文件 | 上下文检查、调用安全、版本匹配、面板 ID 与焦点规则 | `research/skill-source.txt` |
| 11 | 官方仓库界面 PNG | 正文图 2，旧界面中可见 Pi、Claude Code | `images/01-herdr-official-interface.png` |
| 12 | 官网 Open Graph 宣传 PNG | 正文图 1；只用于产品介绍，不作为功能验证证据 | `images/02-herdr-official-overview.png` |

原始链接与解析后的链接见 `research/citations.json`、`research/retrieval.json`，正文文末也保留实际引用链接。为避免网页内容修改后无法追溯，文本副本和响应 SHA-256 已留存。响应 SHA-256 对应下载时的响应字节，文本副本经过 HTML 标签清理，不应直接拿文本副本哈希与响应哈希比较。

## 版本边界

- 查阅时官方文档导航标注 Latest 0.9.5；官方 GitHub latest release API 返回 `v0.9.5`，发布字段为 `2026-10-14T16:07:28Z`，见 `research/release.json`。
- 文档网页、仓库 `master` 和发行二进制不是同一种证据。本文没有安装或运行 v0.9.5，不保证页面后续变更与该二进制逐项一致。
- 安装与控制接口以读者当前 `herdr --help`、`herdr --skill` 为复核入口；不使用截图中的旧版命令作为现行语法依据。
- 不声称本文测试过任何 Claude Code、Codex 或 OpenCode 版本，也不声称验证过认证与模型兼容性。

## 图片来源、授权与处理

两张图片均经网络下载并实际打开检查，未裁剪、未标注、未修改；来源与 SHA-256 见 `images/image-manifest.json`。图 2 来源于 Apache-2.0 项目仓库，仓库 LICENSE 已查阅并保留；图 1 来源于官网，不因图上出现 Apache 2.0 字样就推断网站所有素材都具有独立授权声明。

正文保留清楚署名和引用。图片权利仍归原权利人。公开发布前应复核官网宣传素材的转载条件；如需严格消除该授权不确定性，可去掉宣传图，保留有仓库来源的界面截图并按适用许可归属要求处理。商标使用不因代码开源而自动获授额外权利。

图 2 可见公开项目路径、项目演示内容和界面版本信息，未发现明显密钥或个人凭据。不将其描述成作者亲历、本机运行、当前版本截图或三 Agent 完整协作证据。

## 抓取限制与失败记录

本会话 `web_extract` 返回其检索后端不支持正文提取。后续改用 Python requests 直接只读获取官方网页、GitHub 原始文件和 release API，均没有触发软件安装或模型调用。没有把失败的提取操作记为成功。

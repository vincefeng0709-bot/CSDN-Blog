# 参考资料

## 外部资料（已查阅核实）

1. **OpenAI Codex 官方文档 — Skills**
   - 标题：Build skills / developers.openai.com/codex/skills.md
   - 链接：https://developers.openai.com/codex/skills.md
   - 访问日期：2026-11-12
   - 支持结论：Codex 的 skill 是含 `SKILL.md` 的文件夹，frontmatter 必填 `name` + `description`；本地 skill 位置为仓库级 `$CWD/.agents/skills`（向上扫描至仓库根）与个人级 `$HOME/.agents/skills`；显式触发用 `/skills` 或 `$名称`，隐式触发依据 description 匹配；Codex 会在技能较多时缩短 description；修改后需重启生效。

2. **Anthropic 官方文档 — Agent Skills overview / Claude Code skills**
   - 链接：https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview （其中指向 https://code.claude.com/docs/en/skills）
   - 访问日期：2026-11-12
   - 支持结论：Claude Code 支持自定义 Skill，形式为含 `SKILL.md` 的文件夹，自动发现与加载。

3. **Agent Skills 开放标准**
   - 标题：agentskills.io Specification
   - 链接：https://agentskills.io/specification
   - 访问日期：2026-11-12（经 Codex 相关资料交叉确认；规范页本身未逐条核对原文，字段细节以引用资料转述为准）
   - 支持结论：SKILL.md 标准：`name`（小写字母/数字/连字符，须与文件夹名一致）、`description`（必填）必填，`license`、`compatibility` 等选填；建议 SKILL.md 不超过 500 行，细节放入 `references/`。

4. **实例论文（skill 的实际输入）**
   - 标题：External Validation of AI-Assisted Colposcopy Using WHO Dataset for Cervical Precancer and Cancer Detection
   - 作者：Wu T, Wang Y, Cui X, Huang Y, Wu X, Wu J, Xue P, Qiao Y
   - 期刊：npj Digital Medicine，2026，Article in Press，Open Access（CC BY-NC-ND 4.0）
   - DOI：10.1038/s41746-026-02961-3
   - 本地文件：`example/s41746-026-02961-3_reference.pdf`
   - 访问日期：2026-11-12（用户提供）
   - 支持结论：文章第五节所述实例内容（187 例 / 855 图 / 45 名医师 / ΔAUC 等数字）均出自该论文 PDF 及由 skill 生成的批注页。

## 本地产物（真实生成物）

- `example/AI辅助阴道镜WHO外部验证_双栏批注.html`：用户在本地使用 paper-annotate skill 生成的真实批注页（110 KB，单文件 HTML），已逐节核对：30 个段落批注、五色高亮、sticky 章节导航、底部论证地图均存在；页脚含"批注为个人研读笔记/译文为意译"的声明。
- `code/paper-annotate-SKILL.md`：skill 的 SKILL.md 原文（与正文第三节引用内容一致）。

## 本地图片（images/）

均截取自 skill 真实生成的实例页面 `example/AI辅助阴道镜WHO外部验证_双栏批注.html`，2026-11-12 用浏览器实拍（非示意图、非 mock）：

| 文件 | 内容 | 正文位置 |
|------|------|----------|
| `images/01-topbar-abstract.png` | 桌面端 1500px：顶部导航栏、五色图例、摘要段双栏批注 | 第二节 |
| `images/04-mobile-abstract.png` | 移动端 420px：单栏响应式布局的摘要批注 | 第二节 |
| `images/02-results-table2.png` | 结果区：Table 2 与"表格导读"批注 | 第五节 |
| `images/03-overview-map.png` | 底部论证地图与三张总览卡片 | 第五节 |

## 待补充

- 开源仓库地址（用户计划开源，仓库尚未提供）。

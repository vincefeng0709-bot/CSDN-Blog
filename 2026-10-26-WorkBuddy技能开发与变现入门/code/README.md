# WorkBuddy Skill 示例与复现说明

本目录提供原创纯文字 Skill 与本地检查工具，不是已上架商品或实测盈利项目。

## 环境

实际执行检查：Windows 11、Git Bash、Python 3.14.7。`build_skill.py` 与 `test_build_skill.py` 只使用 Python 标准库，无须安装依赖。未在其他 Python 版本实测。

WorkBuddy 客户端安装版本、模型及积分消耗：本次未检查、未执行。不声称已成功导入或自动触发。

## 文件

- `meeting-action-checklist/SKILL.md`：元数据、触发场景和执行边界。
- `meeting-action-checklist/references/rules.md`：提取、日期、冲突和隐私规则。
- `meeting-action-checklist/references/output-format.md`：输出模板。
- `test_materials.md`：合成手工验收用例；不包含模型的实测输出。
- `create-skill-prompt.txt`：与正文一致的创建提示词。
- `build_skill.py`：有限 frontmatter 检查、引用检查、ZIP 生成和回读。
- `test_build_skill.py`：对打包工具的真实端到端测试，不是模型评测。
- `dist/meeting-action-checklist.zip`：本地生成的示例包，仅包含 Skill 目录，不提交生成物；从仓库下载源码后运行打包命令即可生成。

## 本地检查与打包

工作目录：本文章目录，即包含 `article.md` 与 `code/` 的目录，不要求读者使用作者的本地盘符。

以下命令适用于 Git Bash；使用已存在的 Python，不运行联网安装：

```bash
python code/test_build_skill.py
python code/build_skill.py
```

打包工具会覆盖它自己的生成物 `code/dist/meeting-action-checklist.zip`，不会修改原始 Skill，不会登录、上传或发布。需要保留旧包时先复制备份，或使用 `--output` 指定新的 ZIP 路径。

检查器只解析本示例使用的“字段名 + JSON 双引号字符串”这一 YAML 子集，不支持任意 YAML、数组、折叠块或完整平台格式校验。它不检查平台账号权限、模型执行质量或售卖资格。

## 客户端导入与手工验收（待执行）

1. 在官方 WorkBuddy 客户端进入「专家·技能·连接器 → 技能 → 添加技能 → 上传技能」。
2. 选择生成的 ZIP 包。该步骤是安装到自己的客户端，不是向市场公开上架。
3. 在「已安装」确认并启用，创建新会话运行 `test_materials.md` 中各项用例。
4. 保存原始实际输出，再按验收标准逐项检查。
5. 如果导入解析失败，对照当时官方技能规范检查字段、目录层级、引用与包内容；不能把本地检查通过当成平台会接受的保证。

示例 `author` 包含教学占位说明，正式提审前需替换为实际开发者名称并更新相关资料、版本和依赖说明。不要直接售卖未经验证的教学包。

## 隐私与能力边界

本包自身没有联网脚本和连接器，不主动向开发者服务器发送数据，但 WorkBuddy 模型推理及平台服务不等于离线运行。不要用真实敏感会议测试；先脱敏并确认处理权限。

## 作者本地审核工具

`build_review.py`、相关审核测试、HTML 与内部审校记录只在作者本地保留，不属于此公开示例或 Skill ZIP。复现上面的标准库打包与测试不依赖它们，也不需要 `Markdown` 包。HTML 预览不代表 CSDN 编辑器兼容性验证。

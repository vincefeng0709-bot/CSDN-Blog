不用第三方工具：Claude 桌面端官方网关直连 DeepSeek 与 Kimi

Claude 桌面端的交互界面确实好用，但它绑定自家的 Claude 模型，订阅额度一用完就只能干等。很多人的想法其实很直接：界面留下，把底层引擎换成别的模型——比如价格更友好的 DeepSeek，或者长上下文见长的 Kimi。

过去要实现这一点，社区普遍的做法是架一个本地代理或者第三方网关工具，把请求转换协议后转出去，配置繁琐，还要额外维护一个常驻进程。

其实 Claude 桌面端现在内置了官方入口：开启开发者模式后，有一个 **Configure Third-Party Inference（配置第三方推理）** 功能，可以直接把推理请求指向任何兼容 Anthropic Messages 协议的端点。DeepSeek 和 Kimi（Moonshot）都官方提供了 Anthropic 兼容端点，两边一对接就通了，全程不需要任何第三方工具。

本文以 DeepSeek 为主线走通全流程（已在 Windows 11 本机实测），再给出 Kimi 的对应配置，Kimi 的字段取值以其官方文档为准。

## 原理：为什么是"Gateway"

在第三方推理配置界面里，连接方式叫 **Gateway（网关）**：Claude 桌面端不再把推理请求发给 Anthropic 官方服务器，而是发给你指定的 base URL，协议格式仍然是 Anthropic Messages API。

这就解释了为什么接入方必须是"Anthropic 兼容端点"而不能随便填一个 OpenAI 格式的地址：

| 服务商 | Anthropic 兼容 base URL | 说明 |
| --- | --- | --- |
| DeepSeek | `https://api.deepseek.com/anthropic` | 官方文档明确标注为 base_url (Anthropic) |
| Kimi（国内） | `https://api.moonshot.cn/anthropic` | 接口路径为 `/anthropic/v1/messages` |
| Kimi（国际站） | `https://api.moonshot.ai/anthropic` | 与创建 Key 的平台需保持一致 |

这两家本来就是"改个 base_url 就能兼容 Anthropic SDK"的思路，所以 Claude 桌面端这边同样只需换 URL + 填 Key。

## 第一步：开启开发者模式

默认安装的 Claude 桌面端菜单里没有 Developer 项。路径是：

**菜单（左上角三条横线）→ Help → Troubleshooting → Enable Developer Mode**

![在 Help > Troubleshooting 中开启开发者模式](https://i-blog.csdnimg.cn/direct/0519a550993d4f7e9d849def5e51775c.png#pic_center)

点击后应用会重启。重启后菜单栏会多出一个 **Developer** 菜单，里面包含 `Configure Third-Party Inference...`、`Open App Config File...`、`Show Dev Tools` 等调试入口。

## 第二步：打开第三方推理配置界面

**Developer → Configure Third-Party Inference...**

![Developer 菜单中的 Configure Third-Party Inference 项](https://i-blog.csdnimg.cn/direct/c306818718f0427a9fa4097d8c0c6e22.png#pic_center)

这个界面本身就是一个完整的设置页：左侧是 Connection、Workspace restrictions、Connectors & extensions 等分区，右侧是连接配置表单。

## 第三步：新建一个配置

右上角的配置下拉框默认是 `Default`。建议点开后选择 **New configuration** 新建一份，比如命名为 `deepseek`，而不是直接改动 Default：

![通过 New configuration 新建配置项](https://i-blog.csdnimg.cn/direct/527474379f4e492fbe011dce3eb661a8.png#pic_center)

这样做的好处是：官方 Claude 与第三方引擎两套配置并存，随时可以在下拉框里切换回来，互不干扰。

接下来在 Connection 表单里填两个关键字段：

1. **Gateway base URL**：填服务商的 Anthropic 兼容端点，DeepSeek 即 `https://api.deepseek.com/anthropic`。
2. **Credential kind（凭据类型）**：下拉框里有三个选项——Static API key、Interactive sign-in、Helper script。**必须选 Static API key**，也就是把你从 DeepSeek 开放平台申请到的 API Key 以静态凭据的方式填进去。

![Credential kind 选择 Static API key](https://i-blog.csdnimg.cn/direct/b405343b11b047c1ac83632644648186.png#pic_center)

如果一开始不确定端点 URL，直接查服务商的 API 文档。以 DeepSeek 为例，其文档"首次调用 API"页面给出了两个 base_url，其中专门标注给 Anthropic 格式的就是我们要的：

![DeepSeek API 文档中的 Anthropic base_url](https://i-blog.csdnimg.cn/direct/2ff78232496f430188f2301d65b4d402.png#pic_center)

另外表单里还有 **Custom inference headers**（自定义请求头）和 **Model discovery**（是否在启动时从 `/v1/models` 自动拉取模型列表）等高级项，按默认留空即可；模型也可以在后续界面手动指定。

## 第四步：Apply Changes 并切换模型

填完 URL 和 API Key 后点击右下角 **Apply Changes** 保存。回到 Cowork 主界面，在输入框旁的模型选择器里就能看到新引擎的模型了：

![Cowork 模型选择器中出现 DeepSeek 模型](https://i-blog.csdnimg.cn/direct/f5b8e41496ac47c98bd139786324083e.png#pic_center)

选中即用，聊天界面的用法和原来完全一样。左下角也能看到当前生效的连接来源（如 Gateway）。

**实测结果**：作者在 Windows 11 本机按上述流程配置 DeepSeek 后，模型选择器正常出现 DeepSeek 模型，对话正常返回，接入成功。下图为作者本机的 Cowork 主界面，右下角已显示 `deepseek-v4-pro`，左下角连接来源为 Gateway：

![作者本机 Cowork 界面：模型为 deepseek-v4-pro，连接来源为 Gateway](https://i-blog.csdnimg.cn/direct/55ff00f1fce446e38b35213dc82fd610.png#pic_center)

一个小细节：本机截图中的模型名显示为带连字符的 `deepseek-v4-pro`，而部分教程画面中显示为 `deepseekv4-pro`，不同版本的界面命名可能略有差异，以实际拉取到的模型列表为准。

### 可选：用 curl 先验证端点和 Key

如果不想在图形界面里试错，可以先用一条 curl 命令确认端点和 Key 可用（以下为示例方法，非本文实际执行的命令）：

```bash
curl https://api.deepseek.com/anthropic/v1/messages \
  --header "Authorization: Bearer $DEEPSEEK_API_KEY" \
  --header "Content-Type: application/json" \
  --data '{"model": "deepseek-v4-flash", "max_tokens": 16, "messages": [{"role": "user", "content": "hi"}]}'
```

返回正常 JSON 即端点与凭据均可用；返回 401 说明 Key 无效或与平台不匹配。Kimi 同理，把 URL 换成 `https://api.moonshot.cn/anthropic/v1/messages`、模型换成对应的 Kimi 模型即可。

## 接入 Kimi

Kimi 的接入流程与 DeepSeek 完全一致，字段取值以 Kimi 开放平台官方文档为准（[API 概述](https://platform.kimi.com/docs/api/overview)、[在 Claude Code 中使用 Kimi](https://platform.kimi.com/docs/guide/claude-code-kimi)）：

| 配置项 | 取值 |
| --- | --- |
| Gateway base URL | `https://api.moonshot.cn/anthropic` |
| Credential kind | Static API key（Key 在 Kimi 开放平台控制台创建） |
| 模型 | `kimi-k3[1m]`（约百万 token 上下文）、`kimi-k3.1-pro`、`kimi-k2.7-code`、`kimi-k2.6` 等 |

两点提示：

- 国内站（`api.moonshot.cn`）与国际站（`api.moonshot.ai`）的 Key 不通用，base URL 要和创建 Key 的平台一致，否则会得到 401。
- 模型名建议以配置界面的 Model discovery 拉取结果或官方文档为准，Kimi 的模型迭代较快，旧模型名可能下线。

按同样的四步走即可：新建配置 → 填 base URL → 选 Static API key 并填 Key → Apply Changes。模型选择与计费细节以官方文档为准。

## 踩坑与注意事项

- **Credential kind 一定要选 Static API key**。这是最容易出错的一步：Interactive sign-in 走的是交互式登录流程，Helper script 需要外部脚本动态提供凭据，都不是"直接填一个 API Key"的场景，选错会导致鉴权失败。
- **模型名时效性**。DeepSeek 文档已标注 `deepseek-chat`、`deepseek-reasoner` 将于北京时间 2026-07-24 23:59 弃用，由 `deepseek-v4-flash` / `deepseek-v4-pro` 接替。老教程里的模型名照抄可能报"模型不存在"。
- **API Key 是明文存储的**。Static API key 会保存在本机配置文件中，不要把配置文件截图或提交到 Git 仓库；官方 Claude 配置随时可通过配置下拉框切回 Default。
- **配置是可导出的**。配置界面右上角有 Export，可以导出配置在其他机器复用（注意导出文件中同样可能包含凭据）。
- **功能入口依赖开发者模式**。如果菜单里找不到 Developer，先确认第一步的 Enable Developer Mode 已执行并重启了应用。

## 总结

整个接入过程没有一行需要自己写的代码，也不依赖任何常驻代理：开发者模式是官方开关，Gateway 模式是官方支持的连接形态，DeepSeek 和 Kimi 则在服务端做好了 Anthropic 协议兼容。换引擎的成本被压缩到了"一个 URL + 一个 API Key"。

真正的取舍在于：接第三方引擎后，Claude 自家的模型能力（如与 Claude 生态深度绑定的功能）可能表现不同，计费也转到对应服务商的 API 账户，用量和限额要按各平台的文档核算。建议先用 New configuration 的隔离配置小范围试跑，确认稳定性后再日常使用。

# ChatCompletions格式

根据对话历史创建模型响应。支持流式和非流式响应。

兼容 OpenAI Chat Completions API。

## OpenAPI 摘要
### ChatCompletions格式

| 项目 | 值 |
| --- | --- |
| 方法 | `POST` |
| 路径 | `/v1/chat/completions` |
| Operation ID | `createchatcompletion` |
| 标签 | 聊天（Chat）/原生OpenAI格式 |

根据对话历史创建模型响应。支持流式和非流式响应。

兼容 OpenAI Chat Completions API。

#### 认证

| 名称 | 类型 | 方案 | 说明 |
| --- | --- | --- | --- |
| `BearerAuth` | http | bearer | 使用 Bearer Token 认证。<br>格式: `Authorization: Bearer sk-xxxxxx` |

#### 请求体

必填: 是

##### application/json

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| model | string | 是 | 模型 ID<br>示例: `gpt-4` |
| messages | array<object> | 是 | 对话消息列表 |
| messages[].role | string | 是 | 消息角色<br>可选值: `system`, `user`, `assistant`, `tool`, `developer` |
| messages[].content | oneOf(string, array<object>) | 是 | 消息内容 |
| messages[].name | string | 否 | 发送者名称 |
| messages[].tool_calls | array<object> | 否 |  |
| messages[].tool_calls[].id | string | 否 |  |
| messages[].tool_calls[].type | string | 否 | 示例: `function` |
| messages[].tool_calls[].function | object | 否 |  |
| messages[].tool_calls[].function.name | string | 否 |  |
| messages[].tool_calls[].function.arguments | string | 否 |  |
| messages[].tool_call_id | string | 否 | 工具调用 ID（用于 tool 角色消息） |
| messages[].reasoning_content | string | 否 | 推理内容 |
| temperature | number | 否 | 采样温度<br>默认值: `1`<br>最小值: `0`<br>最大值: `2` |
| top_p | number | 否 | 核采样参数<br>默认值: `1`<br>最小值: `0`<br>最大值: `1` |
| n | integer | 否 | 生成数量<br>默认值: `1`<br>最小值: `1` |
| stream | boolean | 否 | 是否流式响应<br>默认值: `False` |
| stream_options | object | 否 |  |
| stream_options.include_usage | boolean | 否 |  |
| stop | oneOf(string, array<string>) | 否 | 停止序列 |
| max_tokens | integer | 否 | 最大生成 Token 数 |
| max_completion_tokens | integer | 否 | 最大补全 Token 数 |
| presence_penalty | number | 否 | 默认值: `0`<br>最小值: `-2`<br>最大值: `2` |
| frequency_penalty | number | 否 | 默认值: `0`<br>最小值: `-2`<br>最大值: `2` |
| logit_bias | object | 否 |  |
| user | string | 否 |  |
| tools | array<object> | 否 |  |
| tools[].type | string | 否 | 示例: `function` |
| tools[].function | object | 否 |  |
| tools[].function.name | string | 否 |  |
| tools[].function.description | string | 否 |  |
| tools[].function.parameters | object | 否 | JSON Schema 格式的参数定义 |
| tool_choice | oneOf(string, object) | 否 |  |
| response_format | object | 否 |  |
| response_format.type | string | 否 | 可选值: `text`, `json_object`, `json_schema` |
| response_format.json_schema | object | 否 | JSON Schema 定义 |
| seed | integer | 否 |  |
| reasoning_effort | string | 否 | 推理强度 (用于支持推理的模型)<br>可选值: `low`, `medium`, `high` |
| modalities | array<string> | 否 |  |
| audio | object | 否 |  |
| audio.voice | string | 否 |  |
| audio.format | string | 否 |  |

#### 响应


##### HTTP 200

成功创建响应

###### application/json

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | string | 否 |  |
| object | string | 否 | 示例: `chat.completion` |
| created | integer | 否 |  |
| model | string | 否 |  |
| choices | array<object> | 否 |  |
| choices[].index | integer | 否 |  |
| choices[].message | object | 否 |  |
| choices[].message.role | string | 是 | 消息角色<br>可选值: `system`, `user`, `assistant`, `tool`, `developer` |
| choices[].message.content | oneOf(string, array<object>) | 是 | 消息内容 |
| choices[].message.name | string | 否 | 发送者名称 |
| choices[].message.tool_calls | array<object> | 否 |  |
| choices[].message.tool_calls[].id | string | 否 |  |
| choices[].message.tool_calls[].type | string | 否 | 示例: `function` |
| choices[].message.tool_calls[].function | object | 否 |  |
| choices[].message.tool_calls[].function.name | string | 否 |  |
| choices[].message.tool_calls[].function.arguments | string | 否 |  |
| choices[].message.tool_call_id | string | 否 | 工具调用 ID（用于 tool 角色消息） |
| choices[].message.reasoning_content | string | 否 | 推理内容 |
| choices[].finish_reason | string | 否 | 可选值: `stop`, `length`, `tool_calls`, `content_filter` |
| usage | object | 否 |  |
| usage.prompt_tokens | integer | 否 | 提示词 Token 数 |
| usage.completion_tokens | integer | 否 | 补全 Token 数 |
| usage.total_tokens | integer | 否 | 总 Token 数 |
| usage.prompt_tokens_details | object | 否 |  |
| usage.prompt_tokens_details.cached_tokens | integer | 否 |  |
| usage.prompt_tokens_details.text_tokens | integer | 否 |  |
| usage.prompt_tokens_details.audio_tokens | integer | 否 |  |
| usage.prompt_tokens_details.image_tokens | integer | 否 |  |
| usage.completion_tokens_details | object | 否 |  |
| usage.completion_tokens_details.text_tokens | integer | 否 |  |
| usage.completion_tokens_details.audio_tokens | integer | 否 |  |
| usage.completion_tokens_details.reasoning_tokens | integer | 否 |  |
| system_fingerprint | string | 否 |  |

##### HTTP 400

请求参数错误

###### application/json

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| error | object | 否 |  |
| error.message | string | 否 | 错误信息 |
| error.type | string | 否 | 错误类型 |
| error.param | string \| null | 否 | 相关参数 |
| error.code | string \| null | 否 | 错误代码 |

##### HTTP 429

请求频率限制

###### application/json

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| error | object | 否 |  |
| error.message | string | 否 | 错误信息 |
| error.type | string | 否 | 错误类型 |
| error.param | string \| null | 否 | 相关参数 |
| error.code | string \| null | 否 | 错误代码 |

## OpenAPI 源文件

`openapi/generated/ai-model/聊天（Chat）/原生OpenAI格式/post-v1-chat-completions-createchatcompletion-383826473.json`

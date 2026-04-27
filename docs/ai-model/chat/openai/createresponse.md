# Responses格式

OpenAI Responses API，用于创建模型响应。
支持多轮对话、工具调用、推理等功能。

## OpenAPI 摘要
### Responses格式

| 项目 | 值 |
| --- | --- |
| 方法 | `POST` |
| 路径 | `/v1/responses` |
| Operation ID | `createresponse` |
| 标签 | 聊天（Chat）/原生OpenAI格式 |

OpenAI Responses API，用于创建模型响应。
支持多轮对话、工具调用、推理等功能。

#### 认证

| 名称 | 类型 | 方案 | 说明 |
| --- | --- | --- | --- |
| `BearerAuth` | http | bearer | 使用 Bearer Token 认证。<br>格式: `Authorization: Bearer sk-xxxxxx` |

#### 请求体

必填: 是

##### application/json

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| model | string | 是 |  |
| input | oneOf(string, array<object>) | 否 | 输入内容，可以是字符串或消息数组 |
| instructions | string | 否 |  |
| max_output_tokens | integer | 否 |  |
| temperature | number | 否 |  |
| top_p | number | 否 |  |
| stream | boolean | 否 |  |
| tools | array<object> | 否 |  |
| tool_choice | oneOf(string, object) | 否 |  |
| reasoning | object | 否 |  |
| reasoning.effort | string | 否 | 可选值: `low`, `medium`, `high` |
| reasoning.summary | string | 否 |  |
| previous_response_id | string | 否 |  |
| truncation | string | 否 | 可选值: `auto`, `disabled` |

#### 响应


##### HTTP 200

成功创建响应

###### application/json

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | string | 否 |  |
| object | string | 否 | 示例: `response` |
| created_at | integer | 否 |  |
| status | string | 否 | 可选值: `completed`, `failed`, `in_progress`, `incomplete` |
| model | string | 否 |  |
| output | array<object> | 否 |  |
| output[].type | string | 否 |  |
| output[].id | string | 否 |  |
| output[].status | string | 否 |  |
| output[].role | string | 否 |  |
| output[].content | array<object> | 否 |  |
| output[].content[].type | string | 否 |  |
| output[].content[].text | string | 否 |  |
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

## OpenAPI 源文件

`openapi/generated/ai-model/聊天（Chat）/原生OpenAI格式/post-v1-responses-createresponse-383826475.json`

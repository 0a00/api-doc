# 原生OpenAI格式

基于给定提示创建文本补全

## OpenAPI 摘要
### 原生OpenAI格式

| 项目 | 值 |
| --- | --- |
| 方法 | `POST` |
| 路径 | `/v1/completions` |
| Operation ID | `createcompletion` |
| 标签 | 补全（Completions） |

基于给定提示创建文本补全

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
| prompt | oneOf(string, array<string>) | 是 |  |
| max_tokens | integer | 否 |  |
| temperature | number | 否 |  |
| top_p | number | 否 |  |
| n | integer | 否 |  |
| stream | boolean | 否 |  |
| stop | oneOf(string, array<string>) | 否 |  |
| suffix | string | 否 |  |
| echo | boolean | 否 |  |

#### 响应


##### HTTP 200

成功创建响应

###### application/json

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | string | 否 |  |
| object | string | 否 | 示例: `text_completion` |
| created | integer | 否 |  |
| model | string | 否 |  |
| choices | array<object> | 否 |  |
| choices[].text | string | 否 |  |
| choices[].index | integer | 否 |  |
| choices[].finish_reason | string | 否 |  |
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

`openapi/generated/ai-model/补全（Completions）/post-v1-completions-createcompletion-383826474.json`

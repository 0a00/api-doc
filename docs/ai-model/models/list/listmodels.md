# 原生OpenAI格式

获取当前可用的模型列表。

根据请求头自动识别返回格式：
- 包含 `x-api-key` 和 `anthropic-version` 头时返回 Anthropic 格式
- 包含 `x-goog-api-key` 头或 `key` 查询参数时返回 Gemini 格式
- 其他情况返回 OpenAI 格式

## OpenAPI 摘要
### 原生OpenAI格式

| 项目 | 值 |
| --- | --- |
| 方法 | `GET` |
| 路径 | `/v1/models` |
| Operation ID | `listmodels` |
| 标签 | 模型（Models）/列出模型 |

获取当前可用的模型列表。

根据请求头自动识别返回格式：
- 包含 `x-api-key` 和 `anthropic-version` 头时返回 Anthropic 格式
- 包含 `x-goog-api-key` 头或 `key` 查询参数时返回 Gemini 格式
- 其他情况返回 OpenAI 格式

#### 认证

| 名称 | 类型 | 方案 | 说明 |
| --- | --- | --- | --- |
| `BearerAuth` | http | bearer | 使用 Bearer Token 认证。<br>格式: `Authorization: Bearer sk-xxxxxx` |

#### 参数

| 名称 | 位置 | 必填 | 类型 | 说明 |
| --- | --- | --- | --- | --- |
| `key` | query | 否 | string | Google API Key (用于 Gemini 格式) |
| `x-api-key` | header | 否 | string | Anthropic API Key (用于 Claude 格式) |
| `anthropic-version` | header | 否 | string | Anthropic API 版本 |
| `x-goog-api-key` | header | 否 | string | Google API Key (用于 Gemini 格式) |

#### 响应


##### HTTP 200

成功获取模型列表

###### application/json

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| object | string | 否 | 示例: `list` |
| data | array<object> | 否 |  |
| data[].id | string | 否 | 模型 ID<br>示例: `gpt-4` |
| data[].object | string | 否 | 对象类型<br>示例: `model` |
| data[].created | integer | 否 | 创建时间戳 |
| data[].owned_by | string | 否 | 模型所有者<br>示例: `openai` |

##### HTTP 401

认证失败

###### application/json

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| error | object | 否 |  |
| error.message | string | 否 | 错误信息 |
| error.type | string | 否 | 错误类型 |
| error.param | string \| null | 否 | 相关参数 |
| error.code | string \| null | 否 | 错误代码 |

## OpenAPI 源文件

`openapi/generated/ai-model/模型（Models）/列出模型/get-v1-models-listmodels-383826468.json`

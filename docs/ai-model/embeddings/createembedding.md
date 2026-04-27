# 原生OpenAI格式

将文本转换为向量嵌入

## OpenAPI 摘要
### 原生OpenAI格式

| 项目 | 值 |
| --- | --- |
| 方法 | `POST` |
| 路径 | `/v1/embeddings` |
| Operation ID | `createembedding` |
| 标签 | 嵌入（Embeddings） |

将文本转换为向量嵌入

#### 认证

| 名称 | 类型 | 方案 | 说明 |
| --- | --- | --- | --- |
| `BearerAuth` | http | bearer | 使用 Bearer Token 认证。<br>格式: `Authorization: Bearer sk-xxxxxx` |

#### 请求体

必填: 是

##### application/json

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| model | string | 是 | 示例: `text-embedding-ada-002` |
| input | oneOf(string, array<string>) | 是 | 要嵌入的文本 |
| encoding_format | string | 否 | 可选值: `float`, `base64`<br>默认值: `float` |
| dimensions | integer | 否 | 输出向量维度 |

#### 响应


##### HTTP 200

成功创建嵌入

###### application/json

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| object | string | 否 | 示例: `list` |
| data | array<object> | 否 |  |
| data[].object | string | 否 | 示例: `embedding` |
| data[].index | integer | 否 |  |
| data[].embedding | array<number> | 否 |  |
| model | string | 否 |  |
| usage | object | 否 |  |
| usage.prompt_tokens | integer | 否 |  |
| usage.total_tokens | integer | 否 |  |

## OpenAPI 源文件

`openapi/generated/ai-model/嵌入（Embeddings）/post-v1-embeddings-createembedding-383826477.json`

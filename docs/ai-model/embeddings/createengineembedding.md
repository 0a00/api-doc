# 原生Gemini格式

使用指定引擎/模型创建嵌入

## OpenAPI 摘要
### 原生Gemini格式

| 项目 | 值 |
| --- | --- |
| 方法 | `POST` |
| 路径 | `/v1/engines/{model}/embeddings` |
| Operation ID | `createengineembedding` |
| 标签 | 嵌入（Embeddings） |

使用指定引擎/模型创建嵌入

#### 认证

| 名称 | 类型 | 方案 | 说明 |
| --- | --- | --- | --- |
| `BearerAuth` | http | bearer | 使用 Bearer Token 认证。<br>格式: `Authorization: Bearer sk-xxxxxx` |

#### 参数

| 名称 | 位置 | 必填 | 类型 | 说明 |
| --- | --- | --- | --- | --- |
| `model` | path | 是 | string | 模型/引擎 ID |

#### 请求体

必填: 否

##### application/json

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| model | string | 是 | 示例: `text-embedding-ada-002` |
| input | oneOf(string, array<string>) | 是 | 要嵌入的文本 |
| encoding_format | string | 否 | 可选值: `float`, `base64`<br>默认值: `float` |
| dimensions | integer | 否 | 输出向量维度 |

#### 调用案例

```bash
curl -X POST "https://你的newapi服务器地址/v1/engines/gpt-4o/embeddings" \
  -H "Authorization: Bearer $NEWAPI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "model": "gpt-4o",
  "input": "New API 是什么？"
}'
```

#### 成功响应示例

```json
{
  "object": "list",
  "data": [
    {
      "object": "embedding",
      "index": 1,
      "embedding": [
        1
      ]
    }
  ],
  "model": "gpt-4o",
  "usage": {
    "prompt_tokens": 1,
    "total_tokens": 1
  }
}
```

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

`openapi/generated/ai-model/嵌入（Embeddings）/post-v1-engines-model-embeddings-createengineembedding-383826478.json`

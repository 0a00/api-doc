# 文档重排序

根据查询对文档列表进行相关性重排序

## OpenAPI 摘要
### 文档重排序

| 项目 | 值 |
| --- | --- |
| 方法 | `POST` |
| 路径 | `/v1/rerank` |
| Operation ID | `creatererank` |
| 标签 | 重排序（Rerank） |

根据查询对文档列表进行相关性重排序

#### 认证

| 名称 | 类型 | 方案 | 说明 |
| --- | --- | --- | --- |
| `BearerAuth` | http | bearer | 使用 Bearer Token 认证。<br>格式: `Authorization: Bearer sk-xxxxxx` |

#### 请求体

必填: 是

##### application/json

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| model | string | 是 | 示例: `rerank-english-v2.0` |
| query | string | 是 | 查询文本 |
| documents | array<oneOf(string, object)> | 是 | 要重排序的文档列表 |
| top_n | integer | 否 | 返回前 N 个结果 |
| return_documents | boolean | 否 | 默认值: `False` |

#### 调用案例

```bash
curl -X POST "https://你的newapi服务器地址/v1/rerank" \
  -H "Authorization: Bearer $NEWAPI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "model": "gpt-4o",
  "query": "string",
  "documents": [
    "string"
  ]
}'
```

#### 成功响应示例

```json
{
  "id": "task_123456",
  "results": [
    {
      "index": 1,
      "relevance_score": 1,
      "document": {}
    }
  ],
  "meta": {}
}
```

#### 响应


##### HTTP 200

成功重排序

###### application/json

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | string | 否 |  |
| results | array<object> | 否 |  |
| results[].index | integer | 否 |  |
| results[].relevance_score | number | 否 |  |
| results[].document | object | 否 |  |
| meta | object | 否 |  |

## OpenAPI 源文件

`openapi/generated/ai-model/重排序（Rerank）/post-v1-rerank-creatererank-383826486.json`

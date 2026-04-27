# 原生OpenAI格式

检查文本内容是否违反使用政策

## OpenAPI 摘要
### 原生OpenAI格式

| 项目 | 值 |
| --- | --- |
| 方法 | `POST` |
| 路径 | `/v1/moderations` |
| Operation ID | `createmoderation` |
| 标签 | 审查（Moderations） |

检查文本内容是否违反使用政策

#### 认证

| 名称 | 类型 | 方案 | 说明 |
| --- | --- | --- | --- |
| `BearerAuth` | http | bearer | 使用 Bearer Token 认证。<br>格式: `Authorization: Bearer sk-xxxxxx` |

#### 请求体

必填: 是

##### application/json

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| input | oneOf(string, array<string>) | 是 |  |
| model | string | 否 | 示例: `text-moderation-latest` |

#### 调用案例

```bash
curl -X POST "https://你的newapi服务器地址/v1/moderations" \
  -H "Authorization: Bearer $NEWAPI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "input": "New API 是什么？"
}'
```

#### 成功响应示例

```json
{
  "id": "task_123456",
  "model": "gpt-4o",
  "results": [
    {
      "flagged": false,
      "categories": {},
      "category_scores": {}
    }
  ]
}
```

#### 响应


##### HTTP 200

成功审核

###### application/json

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | string | 否 |  |
| model | string | 否 |  |
| results | array<object> | 否 |  |
| results[].flagged | boolean | 否 |  |
| results[].categories | object | 否 |  |
| results[].category_scores | object | 否 |  |

## OpenAPI 源文件

`openapi/generated/ai-model/审查（Moderations）/post-v1-moderations-createmoderation-383826487.json`

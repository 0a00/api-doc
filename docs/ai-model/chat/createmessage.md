# 原生Claude格式

Anthropic Claude Messages API 格式的请求。
需要在请求头中包含 `anthropic-version`。

## OpenAPI 摘要
### 原生Claude格式

| 项目 | 值 |
| --- | --- |
| 方法 | `POST` |
| 路径 | `/v1/messages` |
| Operation ID | `createmessage` |
| 标签 | 聊天（Chat） |

Anthropic Claude Messages API 格式的请求。
需要在请求头中包含 `anthropic-version`。

#### 认证

| 名称 | 类型 | 方案 | 说明 |
| --- | --- | --- | --- |
| `BearerAuth` | http | bearer | 使用 Bearer Token 认证。<br>格式: `Authorization: Bearer sk-xxxxxx` |

#### 参数

| 名称 | 位置 | 必填 | 类型 | 说明 |
| --- | --- | --- | --- | --- |
| `anthropic-version` | header | 是 | string | Anthropic API 版本 |
| `x-api-key` | header | 否 | string | Anthropic API Key (可选，也可使用 Bearer Token) |

#### 请求体

必填: 否

##### application/json

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| model | string | 是 | 示例: `claude-3-opus-20240229` |
| messages | array<object> | 是 |  |
| messages[].role | string | 是 | 可选值: `user`, `assistant` |
| messages[].content | oneOf(string, array<object>) | 是 |  |
| system | oneOf(string, array<object>) | 否 |  |
| max_tokens | integer | 是 | 最小值: `1` |
| temperature | number | 否 | 最小值: `0`<br>最大值: `1` |
| top_p | number | 否 |  |
| top_k | integer | 否 |  |
| stream | boolean | 否 |  |
| stop_sequences | array<string> | 否 |  |
| tools | array<object> | 否 |  |
| tools[].name | string | 否 |  |
| tools[].description | string | 否 |  |
| tools[].input_schema | object | 否 |  |
| tool_choice | oneOf(object) | 否 |  |
| thinking | object | 否 |  |
| thinking.type | string | 否 | 可选值: `enabled`, `disabled` |
| thinking.budget_tokens | integer | 否 |  |
| metadata | object | 否 |  |
| metadata.user_id | string | 否 |  |

#### 调用案例

```bash
curl -X POST "https://你的newapi服务器地址/v1/messages" \
  -H "Authorization: Bearer $NEWAPI_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "Content-Type: application/json" \
  -d '{
  "model": "gpt-4o",
  "messages": [
    {
      "role": "user",
      "content": "你好，请介绍一下 New API。"
    }
  ],
  "max_tokens": 300
}'
```

#### 成功响应示例

```json
{
  "id": "task_123456",
  "type": "message",
  "role": "assistant",
  "content": "你好，请介绍一下 New API。",
  "model": "gpt-4o",
  "stop_reason": "end_turn"
}
```

#### 响应


##### HTTP 200

成功创建响应

###### application/json

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | string | 否 |  |
| type | string | 否 | 示例: `message` |
| role | string | 否 | 示例: `assistant` |
| content | array<object> | 否 |  |
| content[].type | string | 否 |  |
| content[].text | string | 否 |  |
| model | string | 否 |  |
| stop_reason | string | 否 | 可选值: `end_turn`, `max_tokens`, `stop_sequence`, `tool_use` |
| usage | object | 否 |  |
| usage.input_tokens | integer | 否 |  |
| usage.output_tokens | integer | 否 |  |
| usage.cache_creation_input_tokens | integer | 否 |  |
| usage.cache_read_input_tokens | integer | 否 |  |

## OpenAPI 源文件

`openapi/generated/ai-model/聊天（Chat）/post-v1-messages-createmessage-383826476.json`

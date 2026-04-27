# OpenAI聊天格式

Gemini 图片生成

## OpenAPI 摘要
### OpenAI聊天格式

| 项目 | 值 |
| --- | --- |
| 方法 | `POST` |
| 路径 | `/v1/chat/completions` |
| Operation ID | `geminirelayv1beta-389846313` |
| 标签 | 图像（Images）/原生Gemini格式 |

Gemini 图片生成

#### 认证

| 名称 | 类型 | 方案 | 说明 |
| --- | --- | --- | --- |
| `BearerAuth` | http | bearer | 使用 Bearer Token 认证。<br>格式: `Authorization: Bearer sk-xxxxxx` |

#### 请求体

必填: 否

##### application/json

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| model | string | 是 |  |
| stream | boolean | 是 |  |
| messages | array<object> | 是 |  |
| messages[].role | string | 否 |  |
| messages[].content | string | 否 |  |
| extra_body | object | 否 |  |
| extra_body.google | object | 是 |  |
| extra_body.google.image_config | object | 是 |  |
| extra_body.google.image_config.aspect_ratio | string | 是 |  |
| extra_body.google.image_config.image_size | string | 是 |  |
| contents | array<object> | 是 |  |
| contents[].role | string | 否 |  |
| contents[].parts | array<object> | 否 |  |
| contents[].parts[].text | string | 否 |  |

#### 调用案例

```bash
curl -X POST "https://你的newapi服务器地址/v1/chat/completions" \
  -H "Authorization: Bearer $NEWAPI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "model": "gpt-4o",
  "stream": false,
  "messages": [
    {
      "role": "user",
      "content": "你好，请介绍一下 New API。"
    }
  ],
  "contents": [
    {
      "role": "user",
      "parts": [
        {
          "text": "你好，请介绍一下 New API。"
        }
      ]
    }
  ]
}'
```

#### 成功响应示例

```json
{
  "id": "task_123456",
  "model": "gpt-4o",
  "object": "string",
  "created": 1,
  "choices": [
    {
      "index": 1,
      "message": {
        "role": "assistant",
        "content": "你好，请介绍一下 New API。"
      },
      "finish_reason": "string"
    }
  ],
  "usage": {
    "prompt_tokens": 1,
    "completion_tokens": 1,
    "total_tokens": 1
  }
}
```

#### 响应


##### HTTP 200

成功

###### application/json

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | string | 是 |  |
| model | string | 是 |  |
| object | string | 是 |  |
| created | integer | 是 |  |
| choices | array<object> | 是 |  |
| choices[].index | integer | 否 |  |
| choices[].message | object | 否 |  |
| choices[].message.role | string | 是 |  |
| choices[].message.content | string | 是 |  |
| choices[].finish_reason | string | 否 |  |
| usage | object | 是 |  |
| usage.prompt_tokens | integer | 是 |  |
| usage.completion_tokens | integer | 是 |  |
| usage.total_tokens | integer | 是 |  |

## OpenAPI 源文件

`openapi/generated/ai-model/图像（Images）/原生Gemini格式/post-v1-chat-completions-geminirelayv1beta-389846313-389846313.json`

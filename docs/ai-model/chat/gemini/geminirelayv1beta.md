# Gemini文本聊天

代理 Gemini API 请求。
路径格式: `/v1beta/models/{model_name}:{action}`

例如:
- `/v1beta/models/gemini-2.5-pro:generateContent`
- `/v1beta/models/gemini-2.5-pro:streamGenerateContent?alt=sse`

## OpenAPI 摘要
### Gemini文本聊天

| 项目 | 值 |
| --- | --- |
| 方法 | `POST` |
| 路径 | `/v1beta/models/{model}:generateContent` |
| Operation ID | `geminirelayv1beta` |
| 标签 | 聊天（Chat）/原生Gemini格式 |

代理 Gemini API 请求。
路径格式: `/v1beta/models/{model_name}:{action}`

例如:
- `/v1beta/models/gemini-2.5-pro:generateContent`
- `/v1beta/models/gemini-2.5-pro:streamGenerateContent?alt=sse`

#### 认证

| 名称 | 类型 | 方案 | 说明 |
| --- | --- | --- | --- |
| `BearerAuth` | http | bearer | 使用 Bearer Token 认证。<br>格式: `Authorization: Bearer sk-xxxxxx` |

#### 参数

| 名称 | 位置 | 必填 | 类型 | 说明 |
| --- | --- | --- | --- | --- |
| `model` | path | 是 | string | 模型名称 |

#### 请求体

必填: 否

##### application/json

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| contents | array<object> | 否 |  |
| contents[].role | string | 否 | 可选值: `user`, `model` |
| contents[].parts | array<object> | 否 |  |
| contents[].parts[].text | string | 否 |  |
| contents[].parts[].inlineData | object | 否 |  |
| contents[].parts[].inlineData.mimeType | string | 否 |  |
| contents[].parts[].inlineData.data | string | 否 |  |
| generationConfig | object | 否 |  |
| generationConfig.temperature | number | 否 |  |
| generationConfig.topP | number | 否 |  |
| generationConfig.topK | integer | 否 |  |
| generationConfig.maxOutputTokens | integer | 否 |  |
| generationConfig.stopSequences | array<string> | 否 |  |
| safetySettings | array<object> | 否 |  |
| safetySettings[].category | string | 否 |  |
| safetySettings[].threshold | string | 否 |  |
| tools | array<object> | 否 |  |
| systemInstruction | object | 否 |  |
| systemInstruction.parts | array<object> | 否 |  |

#### 调用案例

```bash
curl -X POST "https://你的newapi服务器地址/v1beta/models/gpt-4o:generateContent" \
  -H "Authorization: Bearer $NEWAPI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "contents": [
    {
      "role": "user",
      "parts": [
        {
          "text": "你好，请介绍一下 New API。"
        }
      ]
    }
  ],
  "generationConfig": {
    "temperature": 0.7,
    "topP": 1,
    "topK": 1,
    "maxOutputTokens": 1,
    "stopSequences": [
      "string"
    ]
  },
  "safetySettings": [
    {
      "category": "string",
      "threshold": "string"
    }
  ],
  "tools": [
    {}
  ],
  "systemInstruction": {
    "parts": [
      {}
    ]
  }
}'
```

#### 成功响应示例

```json
{
  "candidates": [
    {
      "content": "你好，请介绍一下 New API。",
      "finishReason": "string",
      "safetyRatings": [
        {}
      ]
    }
  ],
  "usageMetadata": {
    "promptTokenCount": 1,
    "candidatesTokenCount": 1,
    "totalTokenCount": 1
  }
}
```

#### 响应


##### HTTP 200

成功

###### application/json

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| candidates | array<object> | 否 |  |
| candidates[].content | object | 否 |  |
| candidates[].content.role | string | 否 |  |
| candidates[].content.parts | array<object> | 否 |  |
| candidates[].finishReason | string | 否 |  |
| candidates[].safetyRatings | array<object> | 否 |  |
| usageMetadata | object | 否 |  |
| usageMetadata.promptTokenCount | integer | 否 |  |
| usageMetadata.candidatesTokenCount | integer | 否 |  |
| usageMetadata.totalTokenCount | integer | 否 |  |

## OpenAPI 源文件

`openapi/generated/ai-model/聊天（Chat）/原生Gemini格式/post-v1beta-models-model-generatecontent-geminirelayv1beta-383826489.json`

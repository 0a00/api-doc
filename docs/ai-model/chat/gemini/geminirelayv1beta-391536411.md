# Gemini媒体识别

Gemini图像、PDF、音频、视频识别请求

⚠️注意：仅支持通过 inlineData 以 base64 方式上传图像、PDF、音频、视频，不支持 fileData.fileUri 或 File API。

## OpenAPI 摘要
### Gemini媒体识别

| 项目 | 值 |
| --- | --- |
| 方法 | `POST` |
| 路径 | `/v1beta/models/{model}:generateContent` |
| Operation ID | `geminirelayv1beta-391536411` |
| 标签 | 聊天（Chat）/原生Gemini格式 |

Gemini图像、PDF、音频、视频识别请求

⚠️注意：仅支持通过 inlineData 以 base64 方式上传图像、PDF、音频、视频，不支持 fileData.fileUri 或 File API。

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

`openapi/generated/ai-model/聊天（Chat）/原生Gemini格式/post-v1beta-models-model-generatecontent-geminirelayv1beta-391536411-391536411.json`

# Gemini原生格式

Gemini 图片生成

## OpenAPI 摘要
### Gemini原生格式

| 项目 | 值 |
| --- | --- |
| 方法 | `POST` |
| 路径 | `/v1beta/models/{model}:generateContent/` |
| Operation ID | `geminirelayv1beta-383837589` |
| 标签 | 图像（Images）/原生Gemini格式 |

Gemini 图片生成

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
| contents | array<object> | 是 |  |
| contents[].role | string | 否 |  |
| contents[].parts | array<object> | 否 |  |
| contents[].parts[].text | string | 否 |  |
| generationConfig | object | 是 |  |
| generationConfig.thinkingConfig | object | 否 |  |
| generationConfig.thinkingConfig.includeThoughts | boolean | 是 | 是否返回思考内容 |
| generationConfig.responseModalities | array<string> | 是 |  |
| generationConfig.imageConfig | object | 是 |  |
| generationConfig.imageConfig.aspectRatio | string | 是 |  |
| generationConfig.imageConfig.imageSize | string | 是 |  |

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

`openapi/generated/ai-model/图像（Images）/原生Gemini格式/post-v1beta-models-model-generatecontent-geminirelayv1beta-383837589-383837589.json`

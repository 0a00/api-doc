# 音频翻译

将音频翻译为英文文本

## OpenAPI 摘要
### 音频翻译

| 项目 | 值 |
| --- | --- |
| 方法 | `POST` |
| 路径 | `/v1/audio/translations` |
| Operation ID | `createtranslation` |
| 标签 | 音频（Audio）/原生OpenAI格式 |

将音频翻译为英文文本

#### 认证

| 名称 | 类型 | 方案 | 说明 |
| --- | --- | --- | --- |
| `BearerAuth` | http | bearer | 使用 Bearer Token 认证。<br>格式: `Authorization: Bearer sk-xxxxxx` |

#### 请求体

必填: 是

##### multipart/form-data

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| file | string(binary) | 是 |  |
| model | string | 是 |  |
| prompt | string | 否 |  |
| response_format | string | 否 |  |
| temperature | number | 否 |  |

#### 响应


##### HTTP 200

成功翻译

###### application/json

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 否 |  |

## OpenAPI 源文件

`openapi/generated/ai-model/音频（Audio）/原生OpenAI格式/post-v1-audio-translations-createtranslation-383826484.json`

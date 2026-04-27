# 音频转录

将音频转换为文本

## OpenAPI 摘要
### 音频转录

| 项目 | 值 |
| --- | --- |
| 方法 | `POST` |
| 路径 | `/v1/audio/transcriptions` |
| Operation ID | `createtranscription` |
| 标签 | 音频（Audio）/原生OpenAI格式 |

将音频转换为文本

#### 认证

| 名称 | 类型 | 方案 | 说明 |
| --- | --- | --- | --- |
| `BearerAuth` | http | bearer | 使用 Bearer Token 认证。<br>格式: `Authorization: Bearer sk-xxxxxx` |

#### 请求体

必填: 是

##### multipart/form-data

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| file | string(binary) | 是 | 音频文件 |
| model | string | 是 | 示例: `whisper-1` |
| language | string | 否 | ISO-639-1 语言代码 |
| prompt | string | 否 |  |
| response_format | string | 否 | 可选值: `json`, `text`, `srt`, `verbose_json`, `vtt`<br>默认值: `json` |
| temperature | number | 否 |  |
| timestamp_granularities | array<string> | 否 |  |

#### 调用案例

```bash
curl -X POST "https://你的newapi服务器地址/v1/audio/transcriptions" \
  -H "Authorization: Bearer $NEWAPI_API_KEY" \
  -F "file=@image.png" \
  -F "model=gpt-4o"
```

#### 成功响应示例

```json
{
  "text": "你好，请介绍一下 New API。"
}
```

#### 响应


##### HTTP 200

成功转录

###### application/json

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 否 |  |

## OpenAPI 源文件

`openapi/generated/ai-model/音频（Audio）/原生OpenAI格式/post-v1-audio-transcriptions-createtranscription-383826483.json`

# 文本转语音

将文本转换为音频

## OpenAPI 摘要
### 文本转语音

| 项目 | 值 |
| --- | --- |
| 方法 | `POST` |
| 路径 | `/v1/audio/speech` |
| Operation ID | `createspeech` |
| 标签 | 音频（Audio）/原生OpenAI格式 |

将文本转换为音频

#### 认证

| 名称 | 类型 | 方案 | 说明 |
| --- | --- | --- | --- |
| `BearerAuth` | http | bearer | 使用 Bearer Token 认证。<br>格式: `Authorization: Bearer sk-xxxxxx` |

#### 请求体

必填: 是

##### application/json

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| model | string | 是 | 示例: `tts-1` |
| input | string | 是 | 要转换的文本 |
| voice | string | 是 | 可选值: `alloy`, `echo`, `fable`, `onyx`, `nova`, `shimmer` |
| response_format | string | 否 | 可选值: `mp3`, `opus`, `aac`, `flac`, `wav`, `pcm`<br>默认值: `mp3` |
| speed | number | 否 | 默认值: `1`<br>最小值: `0.25`<br>最大值: `4` |

#### 响应


##### HTTP 200

成功生成音频

###### audio/mpeg

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string(binary) |  |  |

## OpenAPI 源文件

`openapi/generated/ai-model/音频（Audio）/原生OpenAI格式/post-v1-audio-speech-createspeech-383826485.json`

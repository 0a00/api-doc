# 原生OpenAI格式

建立 WebSocket 连接用于实时对话。

**注意**: 这是一个 WebSocket 端点，需要使用 WebSocket 协议连接。

连接 URL 示例: `wss://api.example.com/v1/realtime?model=gpt-4o-realtime`

## OpenAPI 摘要
### 原生OpenAI格式

| 项目 | 值 |
| --- | --- |
| 方法 | `GET` |
| 路径 | `/v1/realtime` |
| Operation ID | `createrealtimesession` |
| 标签 | 实时语音（Realtime） |

建立 WebSocket 连接用于实时对话。

**注意**: 这是一个 WebSocket 端点，需要使用 WebSocket 协议连接。

连接 URL 示例: `wss://api.example.com/v1/realtime?model=gpt-4o-realtime`

#### 认证

| 名称 | 类型 | 方案 | 说明 |
| --- | --- | --- | --- |
| `BearerAuth` | http | bearer | 使用 Bearer Token 认证。<br>格式: `Authorization: Bearer sk-xxxxxx` |

#### 参数

| 名称 | 位置 | 必填 | 类型 | 说明 |
| --- | --- | --- | --- | --- |
| `model` | query | 否 | string | 要使用的模型 |

#### 响应


##### HTTP 101

WebSocket 协议切换

##### HTTP 400

请求错误

###### application/json

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| error | object | 否 |  |
| error.message | string | 否 | 错误信息 |
| error.type | string | 否 | 错误类型 |
| error.param | string \| null | 否 | 相关参数 |
| error.code | string \| null | 否 | 错误代码 |

## OpenAPI 源文件

`openapi/generated/ai-model/实时语音（Realtime）/get-v1-realtime-createrealtimesession-383826490.json`

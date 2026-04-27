# 即梦视频生成

即梦官方 API 格式的视频生成接口。

支持通过 Action 参数指定操作类型：
- `CVSync2AsyncSubmitTask`: 提交视频生成任务
- `CVSync2AsyncGetResult`: 获取任务结果

需要在查询参数中指定 Action 和 Version。

## OpenAPI 摘要
### 即梦视频生成

| 项目 | 值 |
| --- | --- |
| 方法 | `POST` |
| 路径 | `/jimeng/` |
| Operation ID | `createjimengvideo` |
| 标签 | 视频（Videos）/即梦格式 |

即梦官方 API 格式的视频生成接口。

支持通过 Action 参数指定操作类型：
- `CVSync2AsyncSubmitTask`: 提交视频生成任务
- `CVSync2AsyncGetResult`: 获取任务结果

需要在查询参数中指定 Action 和 Version。

#### 认证

| 名称 | 类型 | 方案 | 说明 |
| --- | --- | --- | --- |
| `BearerAuth` | http | bearer | 使用 Bearer Token 认证。<br>格式: `Authorization: Bearer sk-xxxxxx` |

#### 参数

| 名称 | 位置 | 必填 | 类型 | 说明 |
| --- | --- | --- | --- | --- |
| `Action` | query | 是 | string | API 操作类型 |
| `Version` | query | 是 | string | API 版本 |

#### 请求体

必填: 否

##### application/json

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| req_key | string | 否 | 请求类型标识 |
| prompt | string | 否 | 文本描述 |
| binary_data_base64 | array<string> | 否 | Base64 编码的图片数据 |

#### 响应


##### HTTP 200

成功处理请求

###### application/json

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | integer | 否 | 响应码 |
| message | string | 否 | 响应消息 |
| data | object | 否 | 响应数据 |

##### HTTP 400

请求参数错误

###### application/json

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| error | object | 否 |  |
| error.message | string | 否 | 错误信息 |
| error.type | string | 否 | 错误类型 |
| error.param | string \| null | 否 | 相关参数 |
| error.code | string \| null | 否 | 错误代码 |

## OpenAPI 源文件

`openapi/generated/ai-model/视频（Videos）/即梦格式/post-jimeng-createjimengvideo-383844643.json`

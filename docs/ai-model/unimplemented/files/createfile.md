# 上传文件 (未实现)

此接口尚未实现

## OpenAPI 摘要
### 上传文件 (未实现)

| 项目 | 值 |
| --- | --- |
| 方法 | `POST` |
| 路径 | `/v1/files` |
| Operation ID | `createfile` |
| 标签 | 未实现（Unimplemented）/文件（Files） |

此接口尚未实现

#### 认证

| 名称 | 类型 | 方案 | 说明 |
| --- | --- | --- | --- |
| `BearerAuth` | http | bearer | 使用 Bearer Token 认证。<br>格式: `Authorization: Bearer sk-xxxxxx` |

#### 请求体

必填: 否

##### multipart/form-data

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| file | string(binary) | 否 |  |
| purpose | string | 否 |  |

#### 响应


##### HTTP 501

未实现

###### application/json

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| error | object | 否 |  |
| error.message | string | 否 | 错误信息 |
| error.type | string | 否 | 错误类型 |
| error.param | string \| null | 否 | 相关参数 |
| error.code | string \| null | 否 | 错误代码 |

## OpenAPI 源文件

`openapi/generated/ai-model/未实现（Unimplemented）/文件（Files）/post-v1-files-createfile-383826492.json`

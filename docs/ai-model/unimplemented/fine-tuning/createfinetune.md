# 创建微调任务 (未实现)

此接口尚未实现

## OpenAPI 摘要
### 创建微调任务 (未实现)

| 项目 | 值 |
| --- | --- |
| 方法 | `POST` |
| 路径 | `/v1/fine-tunes` |
| Operation ID | `createfinetune` |
| 标签 | 未实现（Unimplemented）/微调（Fine-tuning） |

此接口尚未实现

#### 认证

| 名称 | 类型 | 方案 | 说明 |
| --- | --- | --- | --- |
| `BearerAuth` | http | bearer | 使用 Bearer Token 认证。<br>格式: `Authorization: Bearer sk-xxxxxx` |

#### 请求体

必填: 否

##### application/json

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | object |  |  |

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

`openapi/generated/ai-model/未实现（Unimplemented）/微调（Fine-tuning）/post-v1-fine-tunes-createfinetune-383826497.json`

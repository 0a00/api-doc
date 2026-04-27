# 列出文件 (未实现)

此接口尚未实现

## OpenAPI 摘要
### 列出文件 (未实现)

| 项目 | 值 |
| --- | --- |
| 方法 | `GET` |
| 路径 | `/v1/files` |
| Operation ID | `listfiles` |
| 标签 | 未实现（Unimplemented）/文件（Files） |

此接口尚未实现

#### 认证

| 名称 | 类型 | 方案 | 说明 |
| --- | --- | --- | --- |
| `BearerAuth` | http | bearer | 使用 Bearer Token 认证。<br>格式: `Authorization: Bearer sk-xxxxxx` |

#### 调用案例

```bash
curl -X GET "https://你的newapi服务器地址/v1/files" \
  -H "Authorization: Bearer $NEWAPI_API_KEY"
```

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

`openapi/generated/ai-model/未实现（Unimplemented）/文件（Files）/get-v1-files-listfiles-383826491.json`

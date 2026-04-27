# 原生Gemini格式

以 Gemini API 格式返回可用模型列表

## OpenAPI 摘要
### 原生Gemini格式

| 项目 | 值 |
| --- | --- |
| 方法 | `GET` |
| 路径 | `/v1beta/models` |
| Operation ID | `listmodelsgemini` |
| 标签 | 模型（Models）/列出模型 |

以 Gemini API 格式返回可用模型列表

#### 认证

| 名称 | 类型 | 方案 | 说明 |
| --- | --- | --- | --- |
| `BearerAuth` | http | bearer | 使用 Bearer Token 认证。<br>格式: `Authorization: Bearer sk-xxxxxx` |

#### 调用案例

```bash
curl -X GET "https://你的newapi服务器地址/v1beta/models" \
  -H "Authorization: Bearer $NEWAPI_API_KEY"
```

#### 成功响应示例

```json
{
  "models": [
    "gpt-4o"
  ]
}
```

#### 响应


##### HTTP 200

成功获取模型列表

###### application/json

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| models | array<object> | 否 |  |
| models[].name | string | 否 | 示例: `models/gemini-pro` |
| models[].version | string | 否 |  |
| models[].displayName | string | 否 |  |
| models[].description | string | 否 |  |
| models[].inputTokenLimit | integer | 否 |  |
| models[].outputTokenLimit | integer | 否 |  |
| models[].supportedGenerationMethods | array<string> | 否 |  |

## OpenAPI 源文件

`openapi/generated/ai-model/模型（Models）/列出模型/get-v1beta-models-listmodelsgemini-383826471.json`

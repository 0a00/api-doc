# 生成图像

百炼qwen-image系列图片生成

## OpenAPI 摘要
### 生成图像

| 项目 | 值 |
| --- | --- |
| 方法 | `POST` |
| 路径 | `/v1/images/generations` |
| Operation ID | `createimage` |
| 标签 | 图像（Images）/通义千问OpenAI格式 |

百炼qwen-image系列图片生成

#### 认证

| 名称 | 类型 | 方案 | 说明 |
| --- | --- | --- | --- |
| `BearerAuth` | http | bearer | 使用 Bearer Token 认证。<br>格式: `Authorization: Bearer sk-xxxxxx` |

#### 请求体

必填: 否

##### application/json

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| model | string | 是 |  |
| input | object | 是 |  |
| input.messages | array<object> | 是 |  |
| input.messages[].role | string | 否 |  |
| input.messages[].content | array<object> | 否 |  |
| input.messages[].content[].text | string | 否 |  |
| parameters | object | 否 |  |
| parameters.negative_prompt | string | 否 |  |
| parameters.prompt_extend | boolean | 否 |  |
| parameters.watermark | boolean | 否 |  |
| parameters.size | string | 否 |  |

#### 响应


##### HTTP 200

成功生成图像

###### application/json

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| created | integer | 否 |  |
| data | array<object> | 否 |  |
| data[].url | string | 否 |  |
| data[].b64_json | string | 否 |  |
| data[].revised_prompt | string | 否 |  |

## OpenAPI 源文件

`openapi/generated/ai-model/图像（Images）/通义千问OpenAI格式/post-v1-images-generations-createimage-383833512.json`

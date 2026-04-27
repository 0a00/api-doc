# 编辑图像

在给定原始图像和提示的情况下创建编辑或扩展图像。

## OpenAPI 摘要
### 编辑图像

| 项目 | 值 |
| --- | --- |
| 方法 | `POST` |
| 路径 | `/v1/images/edits/` |
| Operation ID | `post-v1-images-edits` |
| 标签 | 图像（Images）/原生OpenAI格式 |

在给定原始图像和提示的情况下创建编辑或扩展图像。

#### 认证

| 名称 | 类型 | 方案 | 说明 |
| --- | --- | --- | --- |
| `Bearer` | http | bearer |  |

#### 请求体

必填: 否

##### multipart/form-data

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| image | string(binary) | 是 | 要编辑的图像。必须是有效的 PNG 文件，小于 4MB，并且是方形的。如果未提供遮罩，图像必须具有透明度，将用作遮罩。<br>示例: `cmMtdXBsb2FkLTE2ODc4MzMzNDc3NTEtMjA=/31225951_59371037e9_small.png` |
| mask | string(binary) | 否 | 附加图像，其完全透明区域（例如，alpha 为零的区域）指示image应编辑的位置。必须是有效的 PNG 文件，小于 4MB，并且尺寸与原始image相同。<br>示例: `[]` |
| prompt | string | 是 | 所需图像的文本描述。最大长度为 1000 个字符。<br>示例: `A cute baby sea otter wearing a beret.` |
| n | string | 否 | 要生成的图像数。必须介于 1 和 10 之间。<br>示例: `1` |
| size | string | 否 | 生成图像的大小。必须是`256x256`、`512x512`或 `1024x1024`之一。<br>示例: `1024x1024` |
| response_format | string | 否 | 生成的图像返回的格式。必须是`url`或`b64_json`。<br>示例: `url` |
| user | string | 否 | 代表您的最终用户的唯一标识符，可以帮助 OpenAI 监控和检测滥用行为。[了解更多](https://platform.openai.com/docs/guides/safety-best-practices/end-user-ids)。<br>示例: `` |
| model | string | 否 | 示例: `dall-e-2` |

#### 响应


##### HTTP 200

Response

###### application/json

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | object |  |  |

## OpenAPI 源文件

`openapi/generated/ai-model/图像（Images）/原生OpenAI格式/post-v1-images-edits-post-v1-images-edits-385320133.json`

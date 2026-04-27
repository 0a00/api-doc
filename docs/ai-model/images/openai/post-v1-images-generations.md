# 生成图像

在给定提示的情况下创建图像。[了解更多](https://platform.openai.com/docs/guides/images)。

## OpenAPI 摘要
### 生成图像

| 项目 | 值 |
| --- | --- |
| 方法 | `POST` |
| 路径 | `/v1/images/generations/` |
| Operation ID | `post-v1-images-generations` |
| 标签 | 图像（Images）/原生OpenAI格式 |

在给定提示的情况下创建图像。[了解更多](https://platform.openai.com/docs/guides/images)。

#### 认证

| 名称 | 类型 | 方案 | 说明 |
| --- | --- | --- | --- |
| `Bearer` | http | bearer |  |

#### 请求体

必填: 否

##### application/json

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| model | string | 否 | 用于图像生成的模型。`dall-e-2`、`dall-e-3` 或 `gpt-image-1` 之一。默认为 `dall-e-2`，除非使用特定于 `gpt-image-1` 的参数。 |
| prompt | string | 是 | 所需图像的文本描述。`gpt-image-1` 的最大长度为 32000 个字符，`dall-e-2` 的最大长度为 1000 个字符，`dall-e-3` 的最大长度为 4000 个字符。 |
| n | integer | 否 | 要生成的图像数量。必须介于 1 到 10 之间。对于 `dall-e-3`，仅支持 `n=1`。 |
| size | string | 否 | 生成的图像的大小。`对于 gpt-image-1`，必须是 `1024x1024`、`1536x1024`（横向）、`1024x1536`（纵向）或`自动`（默认值）之一，`对于 dall-e-2`，必须是 `256x256、``512x512` 或 `1024x1024` 之一，对于 `dall-e-3`，必须是 `1024x1024`、`1792x1024` 或 `1024x1792` 之一。 |
| background | string | 否 | 允许为生成的图像的背景设置透明度。此参数仅支持 `gpt-image-1`。必须是以下之一 `透明`、`不透明`或`自动`（默认值）。使用`自动`时，模型将自动确定图像的最佳背景。<br><br>如果`是透明`的，则输出格式需要支持透明度，因此应将其设置为 `png`（默认值）或 `webp`。 |
| moderation | string | 否 | 控制 `gpt-image-1` 生成的图像的内容审核级别。必须为`低，` 以进行限制较少的筛选或`自动`（默认值）。 |
| quality | string | 否 | 将生成的图像的质量。 |
| stream | string | 否 |  |
| style | string | 否 |  |
| user | string | 否 |  |

#### 响应


##### HTTP 200

Response

###### application/json

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| created | integer | 是 |  |
| data | array<object> | 是 |  |
| data[].b64_json | string | 否 |  |
| data[].url | string | 是 |  |
| usage | object | 是 |  |
| usage.total_tokens | integer | 是 |  |
| usage.input_tokens | integer | 是 |  |
| usage.output_tokens | integer | 是 |  |
| usage.input_tokens_details | object | 是 |  |
| usage.input_tokens_details.text_tokens | integer | 是 |  |
| usage.input_tokens_details.image_tokens | integer | 是 |  |

## OpenAPI 源文件

`openapi/generated/ai-model/图像（Images）/原生OpenAI格式/post-v1-images-generations-post-v1-images-generations-385320132.json`

# Kling 图生视频

使用 Kling 模型从图片生成视频。

支持通过 image 参数传入图片 URL 或 Base64 编码的图片数据。

## OpenAPI 摘要
### Kling 图生视频

| 项目 | 值 |
| --- | --- |
| 方法 | `POST` |
| 路径 | `/kling/v1/videos/image2video` |
| Operation ID | `createklingimage2video` |
| 标签 | 视频（Videos）/可灵格式 |

使用 Kling 模型从图片生成视频。

支持通过 image 参数传入图片 URL 或 Base64 编码的图片数据。

#### 认证

| 名称 | 类型 | 方案 | 说明 |
| --- | --- | --- | --- |
| `BearerAuth` | http | bearer | 使用 Bearer Token 认证。<br>格式: `Authorization: Bearer sk-xxxxxx` |

#### 请求体

必填: 否

##### application/json

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| model | string | 否 | 模型/风格 ID<br>示例: `kling-v1` |
| prompt | string | 否 | 文本描述提示词<br>示例: `宇航员站起身走了` |
| image | string | 否 | 图片输入 (URL 或 Base64)<br>示例: `https://example.com/image.jpg` |
| duration | number | 否 | 视频时长（秒）<br>示例: `5` |
| width | integer | 否 | 视频宽度<br>示例: `1280` |
| height | integer | 否 | 视频高度<br>示例: `720` |
| fps | integer | 否 | 视频帧率<br>示例: `30` |
| seed | integer | 否 | 随机种子<br>示例: `20231234` |
| n | integer | 否 | 生成视频数量<br>示例: `1` |
| response_format | string | 否 | 响应格式<br>示例: `url` |
| user | string | 否 | 用户标识<br>示例: `user-1234` |
| metadata | object | 否 | 扩展参数 (如 negative_prompt, style, quality_level 等) |

#### 响应


##### HTTP 200

成功创建视频生成任务

###### application/json

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| task_id | string | 否 | 任务 ID<br>示例: `abcd1234efgh` |
| status | string | 否 | 任务状态<br>示例: `queued` |

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

`openapi/generated/ai-model/视频（Videos）/可灵格式/post-kling-v1-videos-image2video-createklingimage2video-383844641.json`

# 创建视频 

OpenAI 兼容的视频生成接口。

参考文档: https://platform.openai.com/docs/api-reference/videos/create

## OpenAPI 摘要
### 创建视频 

| 项目 | 值 |
| --- | --- |
| 方法 | `POST` |
| 路径 | `/v1/videos` |
| Operation ID | `createvideo` |
| 标签 | 视频（Videos）/Sora格式 |

OpenAI 兼容的视频生成接口。

参考文档: https://platform.openai.com/docs/api-reference/videos/create

#### 认证

| 名称 | 类型 | 方案 | 说明 |
| --- | --- | --- | --- |
| `BearerAuth` | http | bearer | 使用 Bearer Token 认证。<br>格式: `Authorization: Bearer sk-xxxxxx` |

#### 请求体

必填: 否

##### multipart/form-data

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

#### 调用案例

```bash
curl -X POST "https://你的newapi服务器地址/v1/videos" \
  -H "Authorization: Bearer $NEWAPI_API_KEY" \
  -F "model=gpt-4o" \
  -F "prompt=A cute baby sea otter wearing a beret." \
  -F "image=@image.png" \
  -F "duration=5" \
  -F "width=1280" \
  -F "height=720"
```

#### 成功响应示例

```json
{
  "id": "task_123456",
  "object": "string",
  "model": "gpt-4o",
  "status": "string",
  "progress": 1,
  "created_at": 1,
  "seconds": "string"
}
```

#### 响应


##### HTTP 200

成功创建视频任务

###### application/json

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | string | 是 | 视频 ID |
| object | string | 是 | 对象类型 |
| model | string | 是 | 使用的模型 |
| status | string | 是 | 任务状态 |
| progress | integer | 是 | 进度百分比 |
| created_at | integer | 是 | 创建时间戳 |
| seconds | string | 是 | 视频时长 |
| completed_at | integer | 否 | 完成时间戳 |
| expires_at | integer | 否 | 过期时间戳 |
| size | string | 否 | 视频尺寸 |
| error | object | 否 | OpenAI 视频错误信息 |
| error.message | string | 否 | 错误信息 |
| error.code | string | 否 | 错误码 |
| metadata | object | 否 | 额外元数据 |

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

`openapi/generated/ai-model/视频（Videos）/Sora格式/post-v1-videos-createvideo-383844578.json`

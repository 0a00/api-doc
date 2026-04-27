# 获取 Kling 文生视频任务状态

查询 Kling 文生视频任务的状态和结果。

## OpenAPI 摘要
### 获取 Kling 文生视频任务状态

| 项目 | 值 |
| --- | --- |
| 方法 | `GET` |
| 路径 | `/kling/v1/videos/text2video/{task_id}` |
| Operation ID | `getklingtext2video` |
| 标签 | 视频（Videos）/可灵格式 |

查询 Kling 文生视频任务的状态和结果。

#### 认证

| 名称 | 类型 | 方案 | 说明 |
| --- | --- | --- | --- |
| `BearerAuth` | http | bearer | 使用 Bearer Token 认证。<br>格式: `Authorization: Bearer sk-xxxxxx` |

#### 参数

| 名称 | 位置 | 必填 | 类型 | 说明 |
| --- | --- | --- | --- | --- |
| `task_id` | path | 是 | string | 任务 ID |

#### 调用案例

```bash
curl -X GET "https://你的newapi服务器地址/kling/v1/videos/text2video/task_123456" \
  -H "Authorization: Bearer $NEWAPI_API_KEY"
```

#### 成功响应示例

```json
{
  "task_id": "task_123456",
  "status": "completed",
  "url": "https://example.com/video.mp4",
  "format": "mp4",
  "metadata": {
    "duration": 5,
    "fps": 30,
    "width": 1280,
    "height": 720,
    "seed": 20231234
  },
  "error": {
    "code": 1,
    "message": "string"
  }
}
```

#### 响应


##### HTTP 200

成功获取任务状态

###### application/json

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| task_id | string | 否 | 任务 ID<br>示例: `abcd1234efgh` |
| status | string | 否 | 任务状态<br>可选值: `queued`, `in_progress`, `completed`, `failed`<br>示例: `completed` |
| url | string | 否 | 视频资源 URL（成功时）<br>示例: `https://example.com/video.mp4` |
| format | string | 否 | 视频格式<br>示例: `mp4` |
| metadata | object | 否 | 视频任务元数据 |
| metadata.duration | number | 否 | 实际生成的视频时长<br>示例: `5` |
| metadata.fps | integer | 否 | 实际帧率<br>示例: `30` |
| metadata.width | integer | 否 | 实际宽度<br>示例: `1280` |
| metadata.height | integer | 否 | 实际高度<br>示例: `720` |
| metadata.seed | integer | 否 | 使用的随机种子<br>示例: `20231234` |
| error | object | 否 | 视频任务错误信息 |
| error.code | integer | 否 | 错误码 |
| error.message | string | 否 | 错误信息 |

##### HTTP 404

任务不存在

###### application/json

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| error | object | 否 |  |
| error.message | string | 否 | 错误信息 |
| error.type | string | 否 | 错误类型 |
| error.param | string \| null | 否 | 相关参数 |
| error.code | string \| null | 否 | 错误代码 |

## OpenAPI 源文件

`openapi/generated/ai-model/视频（Videos）/可灵格式/get-kling-v1-videos-text2video-task-id-getklingtext2video-383844640.json`

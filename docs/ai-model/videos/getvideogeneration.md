# 获取视频生成任务状态

查询视频生成任务的状态和结果。

任务状态：
- `queued`: 排队中
- `in_progress`: 生成中
- `completed`: 已完成
- `failed`: 失败

## OpenAPI 摘要
### 获取视频生成任务状态

| 项目 | 值 |
| --- | --- |
| 方法 | `GET` |
| 路径 | `/v1/video/generations/{task_id}` |
| Operation ID | `getvideogeneration` |
| 标签 | 视频（Videos） |

查询视频生成任务的状态和结果。

任务状态：
- `queued`: 排队中
- `in_progress`: 生成中
- `completed`: 已完成
- `failed`: 失败

#### 认证

| 名称 | 类型 | 方案 | 说明 |
| --- | --- | --- | --- |
| `BearerAuth` | http | bearer | 使用 Bearer Token 认证。<br>格式: `Authorization: Bearer sk-xxxxxx` |

#### 参数

| 名称 | 位置 | 必填 | 类型 | 说明 |
| --- | --- | --- | --- | --- |
| `task_id` | path | 是 | string | 任务 ID |

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

`openapi/generated/ai-model/视频（Videos）/get-v1-video-generations-task-id-getvideogeneration-383844577.json`

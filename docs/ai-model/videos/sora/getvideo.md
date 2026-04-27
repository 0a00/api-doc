# 获取视频任务状态 

OpenAI 兼容的视频任务状态查询接口。

返回视频任务的详细状态信息。

## OpenAPI 摘要
### 获取视频任务状态 

| 项目 | 值 |
| --- | --- |
| 方法 | `GET` |
| 路径 | `/v1/videos/{task_id}` |
| Operation ID | `getvideo` |
| 标签 | 视频（Videos）/Sora格式 |

OpenAI 兼容的视频任务状态查询接口。

返回视频任务的详细状态信息。

#### 认证

| 名称 | 类型 | 方案 | 说明 |
| --- | --- | --- | --- |
| `BearerAuth` | http | bearer | 使用 Bearer Token 认证。<br>格式: `Authorization: Bearer sk-xxxxxx` |

#### 参数

| 名称 | 位置 | 必填 | 类型 | 说明 |
| --- | --- | --- | --- | --- |
| `task_id` | path | 是 | string | 视频任务 ID |

#### 调用案例

```bash
curl -X GET "https://你的newapi服务器地址/v1/videos/task_123456" \
  -H "Authorization: Bearer $NEWAPI_API_KEY"
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

成功获取视频任务状态

###### application/json

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | string | 是 |  |
| object | string | 是 |  |
| model | string | 是 |  |
| status | string | 是 |  |
| progress | integer | 是 |  |
| created_at | integer | 是 |  |
| seconds | string | 是 |  |

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

`openapi/generated/ai-model/视频（Videos）/Sora格式/get-v1-videos-task-id-getvideo-383844579.json`

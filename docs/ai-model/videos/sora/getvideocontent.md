# 获取视频内容

获取已完成视频任务的视频文件内容。

此接口会代理返回视频文件流。

## OpenAPI 摘要
### 获取视频内容

| 项目 | 值 |
| --- | --- |
| 方法 | `GET` |
| 路径 | `/v1/videos/{task_id}/content` |
| Operation ID | `getvideocontent` |
| 标签 | 视频（Videos）/Sora格式 |

获取已完成视频任务的视频文件内容。

此接口会代理返回视频文件流。

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
curl -X GET "https://你的newapi服务器地址/v1/videos/task_123456/content" \
  -H "Authorization: Bearer $NEWAPI_API_KEY"
```

#### 成功响应示例

```text
<video/mp4 响应内容>
```

#### 响应


##### HTTP 200

成功获取视频内容

###### video/mp4

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string(binary) |  |  |

##### HTTP 404

视频不存在或未完成

###### application/json

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| error | object | 否 |  |
| error.message | string | 否 | 错误信息 |
| error.type | string | 否 | 错误类型 |
| error.param | string \| null | 否 | 相关参数 |
| error.code | string \| null | 否 | 错误代码 |

## OpenAPI 源文件

`openapi/generated/ai-model/视频（Videos）/Sora格式/get-v1-videos-task-id-content-getvideocontent-383844580.json`

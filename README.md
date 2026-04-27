# API 文档

本仓库保存静态 API 文档站点产物，并保留可重复同步的 MkDocs 源文件。

## 同步范围

- 上游项目：`QuantumNous/new-api-docs-v1`
- 上游版本：`9a6a817d7f045b73571c7752e26b451afca5781d`
- 文档范围：`content/docs/zh/api/ai-model`
- 页面数量：43 个 AI 模型 API 页面

## 本地构建

```bash
pipenv install
pipenv run python scripts/sync_ai_model_docs.py
pipenv run mkdocs build --clean
bash scripts/publish_site.sh
```

同步脚本会重新生成 `docs/`、`mkdocs.yml` 和引用的 OpenAPI JSON。构建产物会输出到 `.site/`，复制到仓库根目录后即可作为静态站点托管。

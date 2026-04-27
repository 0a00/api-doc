#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


UPSTREAM_URL = "https://github.com/QuantumNous/new-api-docs-v1"
UPSTREAM_REF = "9a6a817d7f045b73571c7752e26b451afca5781d"
AI_MODEL_ROOT = Path("content/docs/zh/api/ai-model")
OPENAPI_ROOT = Path("openapi/generated/ai-model")

ROOT = Path(__file__).resolve().parents[1]
DOCS_DIR = ROOT / "docs"
SYNC_DIR = ROOT / ".sync" / "new-api-docs-v1"

CATEGORY_ORDER = [
    "models",
    "chat",
    "completions",
    "embeddings",
    "images",
    "audio",
    "realtime",
    "rerank",
    "moderations",
    "videos",
    "unimplemented",
]

COMPAT_PAGES = [
    ("openai-chat", "OpenAI Chat", "ai-model/chat/openai/createchatcompletion.md"),
    ("openai-responses", "OpenAI Responses", "ai-model/chat/openai/createresponse.md"),
    ("anthropic-chat", "Anthropic Chat", "ai-model/chat/createmessage.md"),
    ("google-gemini-chat", "Google Gemini Chat", "ai-model/chat/gemini/geminirelayv1beta.md"),
    ("deepseek-reasoning-chat", "DeepSeek Reasoning Chat", "ai-model/chat/openai/createchatcompletion.md"),
    ("openai-embedding", "OpenAI Embedding", "ai-model/embeddings/createembedding.md"),
    ("openai-image", "OpenAI Image", "ai-model/images/openai/post-v1-images-generations.md"),
    ("midjourney-proxy-image", "Midjourney Proxy Image", "ai-model/images/index.md"),
    ("openai-audio", "OpenAI Audio", "ai-model/audio/openai/index.md"),
    ("openai-realtime", "OpenAI Realtime", "ai-model/realtime/createrealtimesession.md"),
    ("cohere-rerank", "Cohere Rerank", "ai-model/rerank/creatererank.md"),
    ("jinaai-rerank", "Jina AI Rerank", "ai-model/rerank/creatererank.md"),
    ("xinference-rerank", "Xinference Rerank", "ai-model/rerank/creatererank.md"),
    ("suno-music", "Suno Music", "ai-model/index.md"),
    ("coming-soon", "Coming Soon", "ai-model/index.md"),
]


@dataclass
class Page:
    source_rel: Path
    out_rel: Path
    title: str


@dataclass
class NavNode:
    title: str
    rel_dir: Path
    pages: list[Page] = field(default_factory=list)
    children: dict[str, "NavNode"] = field(default_factory=dict)


def run(cmd: list[str], cwd: Path = ROOT) -> None:
    subprocess.run(cmd, cwd=cwd, check=True)


def ensure_upstream(ref: str, upstream_dir: Path) -> None:
    upstream_dir.parent.mkdir(parents=True, exist_ok=True)
    if not (upstream_dir / ".git").exists():
        run(["git", "clone", "--depth", "1", UPSTREAM_URL, str(upstream_dir)])
    run(["git", "fetch", "--depth", "1", "origin", "main"], cwd=upstream_dir)
    run(["git", "checkout", "--detach", ref], cwd=upstream_dir)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    text = text.lstrip("\ufeff")
    if not text.startswith("---"):
        return {}, text
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n?", text, re.S)
    if not match:
        return {}, text
    raw = match.group(1)
    meta: dict[str, str] = {}
    for line in raw.splitlines():
        if ":" not in line or line.startswith(" "):
            continue
        key, value = line.split(":", 1)
        meta[key.strip()] = value.strip().strip("'\"")
    return meta, text[match.end() :]


def load_title(path: Path, fallback: str) -> str:
    if not path.exists():
        return fallback
    data = json.loads(path.read_text(encoding="utf-8"))
    return str(data.get("title") or fallback)


def yaml_quote(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def clean_body(body: str) -> str:
    body = re.sub(r"\{/\*.*?\*/\}\s*", "", body, flags=re.S)
    body = re.sub(r"<APIPage\s+.*?/>", "", body, flags=re.S)
    body = re.sub(r"\n{3,}", "\n\n", body)
    return body.strip()


def find_api_page(body: str) -> tuple[str | None, list[dict[str, str]]]:
    match = re.search(
        r'<APIPage\s+document=\{"([^"]+)"\}\s+operations=\{(\[.*?\])\}\s*/>',
        body,
        flags=re.S,
    )
    if not match:
        return None, []
    return match.group(1), json.loads(match.group(2))


def table_escape(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, (dict, list)):
        value = json.dumps(value, ensure_ascii=False, separators=(",", ":"))
    text = str(value).strip()
    text = text.replace("\\", "\\\\").replace("|", "\\|")
    text = text.replace("\r\n", "\n").replace("\n", "<br>")
    return text


def code(value: Any) -> str:
    text = table_escape(value)
    if not text:
        return ""
    return f"`{text}`"


def resolve_ref(schema: dict[str, Any], document: dict[str, Any]) -> dict[str, Any]:
    ref = schema.get("$ref")
    if not isinstance(ref, str) or not ref.startswith("#/"):
        return schema
    current: Any = document
    for part in ref[2:].split("/"):
        current = current[part.replace("~1", "/").replace("~0", "~")]
    return current if isinstance(current, dict) else schema


def schema_type(schema: dict[str, Any], document: dict[str, Any]) -> str:
    schema = resolve_ref(schema, document)
    if "oneOf" in schema:
        return "oneOf(" + ", ".join(schema_type(item, document) for item in schema["oneOf"]) + ")"
    if "anyOf" in schema:
        return "anyOf(" + ", ".join(schema_type(item, document) for item in schema["anyOf"]) + ")"
    if "allOf" in schema:
        return "allOf(" + ", ".join(schema_type(item, document) for item in schema["allOf"]) + ")"
    typ = schema.get("type")
    if isinstance(typ, list):
        base = " | ".join(str(item) for item in typ)
    elif typ == "array":
        items = schema.get("items") if isinstance(schema.get("items"), dict) else {}
        base = f"array<{schema_type(items, document)}>"
    elif typ:
        base = str(typ)
    elif "properties" in schema:
        base = "object"
    else:
        base = "any"
    if schema.get("format"):
        base += f"({schema['format']})"
    return base


def schema_notes(schema: dict[str, Any]) -> str:
    parts: list[str] = []
    if "description" in schema:
        parts.append(str(schema["description"]).strip())
    if schema.get("enum"):
        parts.append("可选值: " + ", ".join(f"`{item}`" for item in schema["enum"]))
    if "default" in schema:
        parts.append("默认值: `" + table_escape(schema["default"]) + "`")
    examples = schema.get("examples")
    if examples:
        shown = examples[:3] if isinstance(examples, list) else [examples]
        parts.append("示例: " + ", ".join(f"`{table_escape(item)}`" for item in shown))
    if "minimum" in schema:
        parts.append(f"最小值: `{schema['minimum']}`")
    if "maximum" in schema:
        parts.append(f"最大值: `{schema['maximum']}`")
    return "<br>".join(part for part in parts if part)


def ordered_properties(schema: dict[str, Any]) -> list[tuple[str, dict[str, Any]]]:
    props = schema.get("properties")
    if not isinstance(props, dict):
        return []
    ordered_names = schema.get("x-apifox-orders")
    if not isinstance(ordered_names, list):
        ordered_names = list(props.keys())
    result: list[tuple[str, dict[str, Any]]] = []
    seen: set[str] = set()
    for name in ordered_names:
        if name in props and isinstance(props[name], dict):
            result.append((name, props[name]))
            seen.add(name)
    for name, value in props.items():
        if name not in seen and isinstance(value, dict):
            result.append((name, value))
    return result


def schema_rows(
    schema: dict[str, Any],
    document: dict[str, Any],
    prefix: str = "",
    required_names: set[str] | None = None,
    depth: int = 0,
    max_depth: int = 4,
) -> list[list[str]]:
    schema = resolve_ref(schema, document)
    required_names = required_names or set(schema.get("required") or [])
    rows: list[list[str]] = []

    if "oneOf" in schema or "anyOf" in schema or "allOf" in schema:
        variants = schema.get("oneOf") or schema.get("anyOf") or schema.get("allOf") or []
        rows.append([prefix or "value", schema_type(schema, document), "", schema_notes(schema)])
        for index, item in enumerate(variants, start=1):
            if isinstance(item, dict) and depth < max_depth:
                rows.extend(schema_rows(item, document, f"{prefix or 'value'}#方案{index}", set(), depth + 1, max_depth))
        return rows

    if schema.get("type") == "array" and isinstance(schema.get("items"), dict):
        rows.append([prefix or "value", schema_type(schema, document), "", schema_notes(schema)])
        items = resolve_ref(schema["items"], document)
        if ordered_properties(items) and depth < max_depth:
            rows.extend(schema_rows(items, document, f"{prefix or 'value'}[]", set(items.get("required") or []), depth + 1, max_depth))
        return rows

    props = ordered_properties(schema)
    if not props:
        rows.append([prefix or "value", schema_type(schema, document), "", schema_notes(schema)])
        return rows

    for name, child in props:
        child = resolve_ref(child, document)
        field_name = f"{prefix}.{name}" if prefix else name
        rows.append([
            field_name,
            schema_type(child, document),
            "是" if name in required_names else "否",
            schema_notes(child),
        ])
        child_props = ordered_properties(child)
        child_items = child.get("items") if isinstance(child.get("items"), dict) else None
        if depth < max_depth and child_props:
            rows.extend(schema_rows(child, document, field_name, set(child.get("required") or []), depth + 1, max_depth))
        elif depth < max_depth and child.get("type") == "array" and child_items and ordered_properties(resolve_ref(child_items, document)):
            rows.extend(schema_rows(child_items, document, f"{field_name}[]", set(resolve_ref(child_items, document).get("required") or []), depth + 1, max_depth))
    return rows


def render_table(headers: list[str], rows: list[list[str]]) -> list[str]:
    if not rows:
        return []
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
    ]
    for row in rows:
        lines.append("| " + " | ".join(table_escape(cell) for cell in row) + " |")
    return lines


def render_parameters(parameters: list[dict[str, Any]], document: dict[str, Any]) -> list[str]:
    rows = []
    for item in parameters:
        schema = item.get("schema") if isinstance(item.get("schema"), dict) else {}
        rows.append([
            code(item.get("name")),
            item.get("in", ""),
            "是" if item.get("required") else "否",
            schema_type(schema, document),
            item.get("description") or schema_notes(schema),
        ])
    return render_table(["名称", "位置", "必填", "类型", "说明"], rows)


def render_schema_section(schema: dict[str, Any], document: dict[str, Any]) -> list[str]:
    rows = schema_rows(schema, document, required_names=set(schema.get("required") or []))
    return render_table(["字段", "类型", "必填", "说明"], rows)


def first_example(schema: dict[str, Any]) -> Any | None:
    if "example" in schema:
        return schema["example"]
    examples = schema.get("examples")
    if isinstance(examples, list):
        for item in examples:
            if item not in (None, "", []):
                return item
    elif examples not in (None, "", []):
        return examples
    return None


def named_example(name: str, schema: dict[str, Any], media_type: str = "application/json") -> Any | None:
    lowered = name.lower()
    if schema.get("format") == "binary":
        return "@image.png" if media_type == "multipart/form-data" else "<binary>"
    if lowered in {"model"}:
        return "gpt-4o"
    if lowered in {"task_id", "id", "video_id"}:
        return "task_123456"
    if lowered in {"messages"}:
        return [{"role": "user", "content": "你好，请介绍一下 New API。"}]
    if lowered in {"role"}:
        return "assistant"
    if lowered in {"contents"}:
        return [{"role": "user", "parts": [{"text": "你好，请介绍一下 New API。"}]}]
    if lowered in {"prompt"}:
        return "A cute baby sea otter wearing a beret."
    if lowered in {"input"}:
        return "New API 是什么？"
    if lowered in {"text", "content"}:
        return "你好，请介绍一下 New API。"
    if lowered in {"image", "mask", "file"}:
        return "@image.png" if media_type == "multipart/form-data" else "https://example.com/image.png"
    if lowered in {"voice"}:
        return "alloy"
    if lowered in {"response_format"}:
        return "url"
    if lowered in {"size"}:
        return "1024x1024"
    if lowered in {"n"}:
        return 1
    if lowered in {"stream"}:
        return False
    if lowered in {"temperature"}:
        return 0.7
    if lowered in {"max_tokens", "max_completion_tokens"}:
        return 300
    if lowered in {"duration"}:
        return 5
    if lowered in {"width"}:
        return 1280
    if lowered in {"height"}:
        return 720
    if lowered in {"fps"}:
        return 30
    if lowered in {"user"}:
        return "user_123"
    return None


def example_value(
    schema: dict[str, Any],
    document: dict[str, Any],
    name: str = "",
    media_type: str = "application/json",
    depth: int = 0,
    max_depth: int = 4,
) -> Any:
    schema = resolve_ref(schema, document)
    named = named_example(name, schema, media_type)
    if named is not None:
        return named
    explicit = first_example(schema)
    if explicit is not None:
        return explicit
    if "default" in schema:
        return schema["default"]
    if schema.get("enum"):
        return schema["enum"][0]
    if "oneOf" in schema or "anyOf" in schema:
        variants = schema.get("oneOf") or schema.get("anyOf") or []
        for item in variants:
            if isinstance(item, dict):
                return example_value(item, document, name, media_type, depth + 1, max_depth)
    if "allOf" in schema:
        merged: dict[str, Any] = {}
        for item in schema.get("allOf") or []:
            if isinstance(item, dict):
                value = example_value(item, document, name, media_type, depth + 1, max_depth)
                if isinstance(value, dict):
                    merged.update(value)
        return merged or {}

    typ = schema.get("type")
    if isinstance(typ, list):
        typ = next((item for item in typ if item != "null"), typ[0] if typ else "string")
    if typ == "array":
        items = schema.get("items") if isinstance(schema.get("items"), dict) else {}
        return [example_value(items, document, name.rstrip("s"), media_type, depth + 1, max_depth)]
    if typ == "object" or "properties" in schema:
        if depth >= max_depth:
            return {}
        props = ordered_properties(schema)
        required = set(schema.get("required") or [])
        selected = [(key, child) for key, child in props if key in required]
        if not selected:
            selected = props[: min(6, len(props))]
        result: dict[str, Any] = {}
        for key, child in selected:
            result[key] = example_value(child, document, key, media_type, depth + 1, max_depth)
        return result
    if typ == "integer":
        return 1
    if typ == "number":
        return 1
    if typ == "boolean":
        return False
    if typ == "string":
        if schema.get("format") == "binary":
            return "@file"
        return "string"
    return "string"


def sample_path(path: str, parameters: list[dict[str, Any]], document: dict[str, Any]) -> str:
    result = path
    for param in parameters:
        if param.get("in") != "path":
            continue
        name = str(param.get("name", "id"))
        schema = param.get("schema") if isinstance(param.get("schema"), dict) else {}
        value = example_value(schema, document, name)
        result = result.replace("{" + name + "}", str(value))
    return result


def request_media(request_body: dict[str, Any] | None) -> tuple[str | None, dict[str, Any]]:
    if not request_body:
        return None, {}
    content = request_body.get("content") if isinstance(request_body.get("content"), dict) else {}
    for preferred in ("application/json", "multipart/form-data", "application/x-www-form-urlencoded"):
        media = content.get(preferred)
        if isinstance(media, dict):
            return preferred, media
    for media_type, media in content.items():
        if isinstance(media, dict):
            return str(media_type), media
    return None, {}


def shell_quote(value: Any) -> str:
    text = str(value)
    return "'" + text.replace("'", "'\"'\"'") + "'"


def render_curl_example(
    path: str,
    method: str,
    parameters: list[dict[str, Any]],
    request_body: dict[str, Any] | None,
    operation: dict[str, Any],
    document: dict[str, Any],
) -> list[str]:
    media_type, media = request_media(request_body)
    schema = media.get("schema") if isinstance(media.get("schema"), dict) else {}
    path_with_examples = sample_path(path, parameters, document)
    query_parts = []
    header_parts = ['-H "Authorization: Bearer $NEWAPI_API_KEY"']
    for param in parameters:
        name = str(param.get("name", "param"))
        location = param.get("in")
        param_schema = param.get("schema") if isinstance(param.get("schema"), dict) else {}
        value = example_value(param_schema, document, name)
        if location == "query" and param.get("required"):
            query_parts.append(f"{name}={value}")
        elif location == "header" and param.get("required"):
            header_parts.append(f'-H "{name}: {value}"')
    if media_type == "application/json":
        header_parts.append('-H "Content-Type: application/json"')
    if query_parts:
        separator = "&" if "?" in path_with_examples else "?"
        path_with_examples = path_with_examples + separator + "&".join(query_parts)

    lines = [f"curl -X {method.upper()} \"https://你的newapi服务器地址{path_with_examples}\" \\"]
    lines.extend([f"  {part} \\" for part in header_parts])

    if media_type == "multipart/form-data":
        sample = example_value(schema, document, media_type=media_type)
        if isinstance(sample, dict):
            for key, value in sample.items():
                if isinstance(value, str) and value.startswith("@"):
                    lines.append(f"  -F \"{key}={value}\" \\")
                else:
                    lines.append(f"  -F \"{key}={value}\" \\")
    elif media_type in {"application/json", "application/x-www-form-urlencoded"} and schema:
        sample = example_value(schema, document, media_type=media_type)
        if media_type == "application/json":
            payload = json.dumps(sample, ensure_ascii=False, indent=2)
            lines.append(f"  -d {shell_quote(payload)} \\")
        elif isinstance(sample, dict):
            for key, value in sample.items():
                lines.append(f"  -d \"{key}={value}\" \\")

    lines[-1] = lines[-1].rstrip(" \\")
    return ["```bash", *lines, "```"]


def render_success_response_example(operation: dict[str, Any], document: dict[str, Any]) -> list[str]:
    responses = operation.get("responses") if isinstance(operation.get("responses"), dict) else {}
    for status, response in responses.items():
        if not str(status).startswith("2") or not isinstance(response, dict):
            continue
        content = response.get("content") if isinstance(response.get("content"), dict) else {}
        media_type, media = next(((mt, m) for mt, m in content.items() if isinstance(m, dict)), (None, None))
        if not media_type or not isinstance(media, dict):
            continue
        schema = media.get("schema") if isinstance(media.get("schema"), dict) else {}
        if not schema:
            continue
        sample = example_value(schema, document, media_type=str(media_type))
        if str(media_type).startswith("application/json"):
            return ["```json", json.dumps(sample, ensure_ascii=False, indent=2), "```"]
        return ["```text", f"<{media_type} 响应内容>", "```"]
    return []


def render_openapi(document_path: Path, operations: list[dict[str, str]], upstream: Path) -> list[str]:
    openapi = json.loads((upstream / document_path).read_text(encoding="utf-8"))
    rendered: list[str] = ["## OpenAPI 摘要"]
    components = openapi.get("components") if isinstance(openapi.get("components"), dict) else {}
    schemes = components.get("securitySchemes") if isinstance(components.get("securitySchemes"), dict) else {}

    for operation_ref in operations:
        path = operation_ref["path"]
        method = operation_ref["method"].lower()
        operation = openapi["paths"][path][method]
        rendered.extend(
            [
                f"### {operation.get('summary') or openapi.get('info', {}).get('title') or path}",
                "",
                "| 项目 | 值 |",
                "| --- | --- |",
                f"| 方法 | `{method.upper()}` |",
                f"| 路径 | `{path}` |",
                f"| Operation ID | `{operation.get('operationId', '')}` |",
                f"| 标签 | {table_escape(', '.join(operation.get('tags') or []))} |",
            ]
        )
        description = (operation.get("description") or "").strip()
        if description:
            rendered.extend(["", description])

        security = operation.get("security") or openapi.get("security") or []
        if security and schemes:
            rows = []
            for entry in security:
                for name in entry:
                    scheme = schemes.get(name, {})
                    rows.append([
                        code(name),
                        scheme.get("type", ""),
                        scheme.get("scheme", ""),
                        scheme.get("description", ""),
                    ])
            rendered.extend(["", "#### 认证", ""])
            rendered.extend(render_table(["名称", "类型", "方案", "说明"], rows))

        params = operation.get("parameters") if isinstance(operation.get("parameters"), list) else []
        if params:
            rendered.extend(["", "#### 参数", ""])
            rendered.extend(render_parameters(params, openapi))

        request_body = operation.get("requestBody") if isinstance(operation.get("requestBody"), dict) else None
        if request_body:
            rendered.extend(["", "#### 请求体", ""])
            rendered.append(f"必填: {'是' if request_body.get('required') else '否'}")
            content = request_body.get("content") if isinstance(request_body.get("content"), dict) else {}
            for media_type, media in content.items():
                rendered.extend(["", f"##### {media_type}", ""])
                schema = media.get("schema") if isinstance(media, dict) and isinstance(media.get("schema"), dict) else {}
                rendered.extend(render_schema_section(schema, openapi))

        rendered.extend(["", "#### 调用案例", ""])
        rendered.extend(render_curl_example(path, method, params, request_body, operation, openapi))

        success_example = render_success_response_example(operation, openapi)
        if success_example:
            rendered.extend(["", "#### 成功响应示例", ""])
            rendered.extend(success_example)

        responses = operation.get("responses") if isinstance(operation.get("responses"), dict) else {}
        if responses:
            rendered.extend(["", "#### 响应", ""])
            for status, response in responses.items():
                rendered.extend(["", f"##### HTTP {status}", ""])
                if isinstance(response, dict) and response.get("description"):
                    rendered.append(str(response["description"]))
                content = response.get("content") if isinstance(response, dict) and isinstance(response.get("content"), dict) else {}
                for media_type, media in content.items():
                    schema = media.get("schema") if isinstance(media, dict) and isinstance(media.get("schema"), dict) else {}
                    if schema:
                        rendered.extend(["", f"###### {media_type}", ""])
                        rendered.extend(render_schema_section(schema, openapi))

    rendered.extend(["", "## OpenAPI 源文件", "", f"`{document_path.as_posix()}`"])
    return rendered


def generate_page(source_file: Path, upstream: Path, out_file: Path, title: str, copied_openapi: set[Path]) -> None:
    meta, body = parse_frontmatter(read_text(source_file))
    title = meta.get("title") or title
    document, operations = find_api_page(body)
    content = [f"# {title}"]
    cleaned = clean_body(body)
    if cleaned:
        content.extend(["", cleaned])
    if document and operations:
        document_path = Path(document)
        copied_openapi.add(document_path)
        content.extend(["", *render_openapi(document_path, operations, upstream)])
    write_text(out_file, "\n".join(content))


def build_tree(pages: list[Page], dir_titles: dict[Path, str]) -> NavNode:
    root = NavNode(dir_titles.get(Path("."), "AI 模型接口"), Path("."))
    for page in pages:
        current = root
        rel_parent = page.source_rel.parent
        current_path = Path(".")
        for part in rel_parent.parts:
            current_path = current_path / part if current_path != Path(".") else Path(part)
            current = current.children.setdefault(part, NavNode(dir_titles.get(current_path, part), current_path))
        current.pages.append(page)
    return root


def sorted_children(node: NavNode) -> list[NavNode]:
    def key(item: NavNode) -> tuple[int, str]:
        first = item.rel_dir.parts[-1] if item.rel_dir.parts else ""
        order = CATEGORY_ORDER.index(first) if first in CATEGORY_ORDER else len(CATEGORY_ORDER)
        return order, item.title

    return sorted(node.children.values(), key=key)


def sorted_pages(node: NavNode) -> list[Page]:
    return sorted(node.pages, key=lambda page: (page.title, page.out_rel.as_posix()))


def page_path(page: Page) -> str:
    return page.out_rel.as_posix()


def emit_nav_node(node: NavNode, indent: int = 0) -> list[str]:
    pad = "  " * indent
    lines = [f"{pad}- {yaml_quote(node.title)}:"]
    lines.append(f"{pad}  - {yaml_quote('概览')}: ai-model/{node.rel_dir.as_posix() + '/' if node.rel_dir != Path('.') else ''}index.md")
    for child in sorted_children(node):
        lines.extend(emit_nav_node(child, indent + 1))
    for page in sorted_pages(node):
        lines.append(f"{pad}  - {yaml_quote(page.title)}: {page_path(page)}")
    return lines


def link_for(target: str, current_dir: Path) -> str:
    target_path = Path(target)
    source_path = current_dir / "index.md"
    return Path("../" * len(current_dir.parts)).joinpath(target_path).as_posix() if current_dir.parts else target_path.as_posix()


def generate_indexes(node: NavNode, docs_dir: Path) -> None:
    index_rel = Path("ai-model") / node.rel_dir / "index.md" if node.rel_dir != Path(".") else Path("ai-model/index.md")
    current_dir = index_rel.parent
    lines = [
        f"# {node.title}",
        "",
        "本页由上游中文 AI 模型 API 文档同步生成。",
        "",
    ]
    children = sorted_children(node)
    pages = sorted_pages(node)
    if children:
        lines.extend(["## 分类", ""])
        for child in children:
            href = link_for((Path("ai-model") / child.rel_dir / "index.md").as_posix(), current_dir)
            lines.append(f"- [{child.title}]({href})")
        lines.append("")
    if pages:
        lines.extend(["## 页面", ""])
        for page in pages:
            href = link_for(page.out_rel.as_posix(), current_dir)
            lines.append(f"- [{page.title}]({href})")
    write_text(docs_dir / index_rel, "\n".join(lines))
    for child in children:
        generate_indexes(child, docs_dir)


def generate_compat_pages(docs_dir: Path) -> list[str]:
    nav = ["  - \"兼容入口\":"]
    for slug, title, target in COMPAT_PAGES:
        out = docs_dir / f"{slug}.md"
        body = "\n".join(
            [
                f"# {title}",
                "",
                "此入口保留用于兼容旧版页面路径；AI 模型 API 文档已同步到新的分类结构。",
                "",
                f"[打开对应文档]({target})",
            ]
        )
        write_text(out, body)
        nav.append(f"    - {yaml_quote(title)}: {slug}.md")
    return nav


def copy_openapi_files(upstream: Path, docs_dir: Path, copied_openapi: set[Path]) -> None:
    for rel_path in sorted(copied_openapi):
        src = upstream / rel_path
        dst = docs_dir / rel_path
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)


def generate_readme(docs_dir: Path, pages: list[Page], ref: str) -> None:
    category_count = len({page.source_rel.parts[0] for page in pages})
    write_text(
        docs_dir / "index.md",
        "\n".join(
            [
                "# API 文档",
                "",
                "此站点同步自上游中文 AI 模型 API 文档，并转换为静态页面。",
                "",
                f"- 同步范围：`content/docs/zh/api/ai-model`",
                f"- 上游版本：`{ref}`",
                f"- API 页面：`{len(pages)}`",
                f"- 一级分类：`{category_count}`",
                "",
                "[查看 AI 模型接口](ai-model/index.md)",
            ]
        ),
    )


def generate_extra_css(docs_dir: Path) -> None:
    write_text(
        docs_dir / "stylesheets/extra.css",
        """
.md-typeset table:not([class]) {
  font-size: 0.72rem;
}

.md-typeset td code,
.md-typeset th code {
  white-space: nowrap;
}

.md-typeset td {
  vertical-align: top;
}
""",
    )


def generate_mkdocs(root_node: NavNode, compat_nav: list[str]) -> None:
    nav_lines = [
        "nav:",
        "  - \"首页\": index.md",
        *emit_nav_node(root_node, 1),
        *compat_nav,
    ]
    text = "\n".join(
        [
            "site_name: API 文档",
            "site_url: http://example.com/",
            "docs_dir: docs",
            "site_dir: .site",
            "use_directory_urls: true",
            "",
            "theme:",
            "  name: material",
            "  language: zh",
            "  features:",
            "    - navigation.sections",
            "    - navigation.indexes",
            "    - navigation.top",
            "    - search.suggest",
            "    - search.highlight",
            "",
            "markdown_extensions:",
            "  - admonition",
            "  - attr_list",
            "  - tables",
            "  - toc:",
            "      permalink: true",
            "  - pymdownx.details",
            "  - pymdownx.superfences",
            "",
            "extra_css:",
            "  - stylesheets/extra.css",
            "",
            "plugins:",
            "  - search:",
            "      lang:",
            "        - zh",
            "        - en",
            "",
            *nav_lines,
        ]
    )
    write_text(ROOT / "mkdocs.yml", text)


def collect_pages(upstream: Path) -> tuple[list[Page], dict[Path, str]]:
    source_root = upstream / AI_MODEL_ROOT
    dir_titles: dict[Path, str] = {Path("."): load_title(source_root / "meta.json", "AI 模型接口")}
    for meta_file in source_root.rglob("meta.json"):
        rel_dir = meta_file.parent.relative_to(source_root)
        dir_titles[rel_dir if rel_dir.parts else Path(".")] = load_title(meta_file, meta_file.parent.name)

    pages: list[Page] = []
    for source_file in sorted(source_root.rglob("*.mdx")):
        rel = source_file.relative_to(source_root)
        meta, _ = parse_frontmatter(read_text(source_file))
        title = meta.get("title") or rel.stem
        out_rel = Path("ai-model") / rel.with_suffix(".md")
        pages.append(Page(source_rel=rel, out_rel=out_rel, title=title))
    return pages, dir_titles


def main() -> None:
    parser = argparse.ArgumentParser(description="Sync Chinese AI model API docs from upstream.")
    parser.add_argument("--ref", default=UPSTREAM_REF)
    parser.add_argument("--upstream-dir", type=Path, default=SYNC_DIR)
    args = parser.parse_args()

    ensure_upstream(args.ref, args.upstream_dir)

    if DOCS_DIR.exists():
        shutil.rmtree(DOCS_DIR)
    DOCS_DIR.mkdir(parents=True)

    pages, dir_titles = collect_pages(args.upstream_dir)
    copied_openapi: set[Path] = set()
    for page in pages:
        generate_page(args.upstream_dir / AI_MODEL_ROOT / page.source_rel, args.upstream_dir, DOCS_DIR / page.out_rel, page.title, copied_openapi)

    root_node = build_tree(pages, dir_titles)
    generate_indexes(root_node, DOCS_DIR)
    copy_openapi_files(args.upstream_dir, DOCS_DIR, copied_openapi)
    generate_readme(DOCS_DIR, pages, args.ref)
    generate_extra_css(DOCS_DIR)
    compat_nav = generate_compat_pages(DOCS_DIR)
    generate_mkdocs(root_node, compat_nav)

    print(f"Synced {len(pages)} AI model API pages and {len(copied_openapi)} OpenAPI files.")


if __name__ == "__main__":
    main()

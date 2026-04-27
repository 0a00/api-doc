#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

rm -rf \
  404.html \
  index.html \
  sitemap.xml \
  sitemap.xml.gz \
  assets \
  search \
  ai-model \
  openapi \
  stylesheets \
  css \
  anthropic-chat \
  cohere-rerank \
  coming-soon \
  deepseek-reasoning-chat \
  google-gemini-chat \
  jinaai-rerank \
  midjourney-proxy-image \
  openai-audio \
  openai-chat \
  openai-embedding \
  openai-image \
  openai-realtime \
  openai-responses \
  suno-music \
  xinference-rerank

cp -a .site/. ./

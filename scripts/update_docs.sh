#!/usr/bin/env bash
# 更新 akshare 原始文档脚本
# 仅同步上游 akshare docs 到本项目的 akshare_docs 目录
# 不修改本项目的 docs/、registry/ 或 SKILL.md

set -euo pipefail

REPO_URL="https://github.com/akfamily/akshare.git"
BRANCH="main"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
RAW_DOCS_DIR="$PROJECT_ROOT/akshare_docs"
TMP_DIR=$(mktemp -d)

cleanup() {
  rm -rf "$TMP_DIR"
}
trap cleanup EXIT

echo "正在从 akshare 仓库下载上游 docs..."

git clone --depth 1 --filter=blob:none --sparse "$REPO_URL" --branch "$BRANCH" "$TMP_DIR/akshare"
cd "$TMP_DIR/akshare"
git sparse-checkout set docs

echo "正在同步到本地 akshare_docs..."

rm -rf "$RAW_DOCS_DIR"
mkdir -p "$RAW_DOCS_DIR"
cp -r "$TMP_DIR/akshare/docs/." "$RAW_DOCS_DIR/"

echo "正在运行结构校验..."
python3 "$PROJECT_ROOT/scripts/validate_skill_docs.py"

echo "更新完成: $RAW_DOCS_DIR"

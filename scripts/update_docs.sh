#!/usr/bin/env bash
# 更新 akshare 文档脚本
# 从 akshare 仓库下载最新的 docs 目录到本项目

set -euo pipefail

REPO_URL="https://github.com/akfamily/akshare.git"
BRANCH="main"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
DOCS_DIR="$PROJECT_ROOT/akshare_docs"
TMP_DIR=$(mktemp -d)

echo "📥 正在从 akshare 仓库下载 docs 目录..."

# 使用 sparse-checkout 只克隆 docs 目录，减少下载量
git clone --depth 1 --filter=blob:none --sparse "$REPO_URL" --branch "$BRANCH" "$TMP_DIR/akshare"
cd "$TMP_DIR/akshare"
git sparse-checkout set docs

echo "📁 正在更新本地 docs 目录..."

# 删除旧的 docs 目录（如果存在）
rm -rf "$DOCS_DIR"

# 复制新的 docs 目录到项目根目录
cp -r "$TMP_DIR/akshare/docs" "$DOCS_DIR"

# 清理临时目录
rm -rf "$TMP_DIR"

echo "✅ 文档更新完成: $DOCS_DIR"

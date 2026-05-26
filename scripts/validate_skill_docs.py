#!/usr/bin/env python3
"""Validate AKShare skill registries and selected docs."""

from __future__ import annotations

import argparse
import inspect
import json
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
TASK_PLAYBOOKS = ROOT / "registry" / "task_playbooks.json"
INTERFACE_CATALOG = ROOT / "registry" / "interface_catalog.json"
SYMBOL_FORMATS = ROOT / "registry" / "symbol_formats.json"
FIELD_GLOSSARY = ROOT / "registry" / "field_glossary.json"
DOC_EXPECTATIONS = {
    "docs/bank.md": ["## 任务路由", "## 高频接口", "## 常见坑"],
    "docs/bond.md": ["## 任务路由", "## 高频接口", "## 常见坑"],
    "docs/currency.md": ["## 任务路由", "## 高频接口", "## 常见坑"],
    "docs/energy.md": ["## 任务路由", "## 高频接口", "## 常见坑"],
    "docs/stock.md": ["## 任务路由", "## 高频接口", "## 常见坑"],
    "docs/fund.md": ["## 任务路由", "## 高频接口", "## 常见坑"],
    "docs/futures.md": ["## 任务路由", "## 高频接口", "## 常见坑"],
    "docs/fx.md": ["## 任务路由", "## 高频接口", "## 常见坑"],
    "docs/index.md": ["## 任务路由", "## 高频接口", "## 常见坑"],
    "docs/interest_rate.md": ["## 任务路由", "## 高频接口", "## 常见坑"],
    "docs/macro.md": ["## 任务路由", "## 高频接口", "## 常见坑"],
    "docs/news_sentiment.md": ["## 任务路由", "## 高频接口", "## 常见坑"],
    "docs/option.md": ["## 任务路由", "## 高频接口", "## 常见坑"],
    "docs/spot.md": ["## 任务路由", "## 高频接口", "## 常见坑"],
    "docs/technical_analysis.md": ["## 任务路由", "## 高频指标", "## 常见坑"],
    "docs/fundamental_analysis.md": ["## 任务路由", "## 高频接口", "## 常见坑"],
}
FORBIDDEN_TEXT = [
    "结论输出建议",
    "回答协议",
    "操作建议",
    "置信度",
    "失效条件",
    "推荐顺序",
    "适合场景",
    "候选列表",
    "市场结论",
    "关注方向",
    "图表规则",
    "可视化图表",
    "筛选决策",
    "市场研判",
    "stock_screening.md",
    "visualization.md",
    "market_regime",
    "macro_environment",
]
FORBIDDEN_SCAN_FILES = [
    ROOT / "SKILL.md",
    ROOT / "registry" / "task_playbooks.json",
] + [ROOT / relative_path for relative_path in DOC_EXPECTATIONS]


EXPECTED_SELECTION_POLICY = "优先使用非东方财富来源接口"


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def require(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def load_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def validate_playbooks(data: dict[str, Any], known_interfaces: set[str]) -> list[str]:
    errors: list[str] = []
    playbooks = data.get("playbooks")
    require(isinstance(playbooks, list) and playbooks, "task_playbooks.json 缺少非空 playbooks 列表", errors)
    if not isinstance(playbooks, list):
        return errors

    seen_types: set[str] = set()
    for item in playbooks:
        task_type = item.get("task_type")
        require(isinstance(task_type, str) and task_type, "存在缺少 task_type 的 playbook", errors)
        if not isinstance(task_type, str) or not task_type:
            continue
        require(task_type not in seen_types, f"task_type 重复: {task_type}", errors)
        seen_types.add(task_type)

        for key in ("aliases", "preferred_docs", "primary_interfaces"):
            value = item.get(key)
            require(isinstance(value, list) and value, f"{task_type} 缺少非空字段: {key}", errors)

        require(isinstance(item.get("goal"), str) and item.get("goal"), f"{task_type} 缺少 goal", errors)

        for doc_path in item.get("preferred_docs", []):
            require((ROOT / doc_path).exists(), f"{task_type} 引用了不存在的文档: {doc_path}", errors)

        for interface_name in item.get("primary_interfaces", []) + item.get("fallback_interfaces", []):
            require(interface_name in known_interfaces, f"{task_type} 引用了未登记接口: {interface_name}", errors)
    return errors


def validate_interface_catalog(data: dict[str, Any]) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    interfaces = data.get("interfaces")
    require(isinstance(interfaces, list) and interfaces, "interface_catalog.json 缺少非空 interfaces 列表", errors)
    if not isinstance(interfaces, list):
        return errors, warnings

    seen_functions: set[str] = set()
    for item in interfaces:
        function = item.get("function")
        require(isinstance(function, str) and function, "存在缺少 function 的接口配置", errors)
        if not isinstance(function, str) or not function:
            continue
        require(function not in seen_functions, f"接口重复登记: {function}", errors)
        seen_functions.add(function)

        for key in ("asset_class", "symbol_format", "date_format", "freshness", "cost"):
            require(isinstance(item.get(key), str) and item.get(key), f"{function} 缺少字符串字段: {key}", errors)

        for key in ("scenarios", "key_fields", "pitfalls", "fallback"):
            value = item.get(key)
            require(isinstance(value, list), f"{function} 字段必须是列表: {key}", errors)
            if isinstance(value, list) and key != "fallback" and not value:
                warnings.append(f"{function} 的 {key} 为空，信息可能不足")

    return errors, warnings


def validate_symbol_formats(data: dict[str, Any], known_interfaces: set[str]) -> list[str]:
    errors: list[str] = []
    formats = data.get("formats")
    require(isinstance(formats, list) and formats, "symbol_formats.json 缺少非空 formats 列表", errors)
    if not isinstance(formats, list):
        return errors

    seen_names: set[str] = set()
    for item in formats:
        name = item.get("name")
        require(isinstance(name, str) and name, "symbol_formats.json 存在缺少 name 的项", errors)
        if not isinstance(name, str) or not name:
            continue
        require(name not in seen_names, f"symbol format 重复: {name}", errors)
        seen_names.add(name)

        for key in ("pattern", "description"):
            require(isinstance(item.get(key), str) and item.get(key), f"{name} 缺少字符串字段: {key}", errors)

        for key in ("examples", "used_by"):
            value = item.get(key)
            require(isinstance(value, list) and value, f"{name} 缺少非空列表字段: {key}", errors)

        for interface_name in item.get("used_by", []):
            require(interface_name in known_interfaces, f"{name} 引用了未登记接口: {interface_name}", errors)
    return errors


def validate_field_glossary(data: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    fields = data.get("fields")
    require(isinstance(fields, list) and fields, "field_glossary.json 缺少非空 fields 列表", errors)
    if not isinstance(fields, list):
        return errors

    seen_fields: set[str] = set()
    for item in fields:
        field = item.get("field")
        require(isinstance(field, str) and field, "field_glossary.json 存在缺少 field 的项", errors)
        if not isinstance(field, str) or not field:
            continue
        require(field not in seen_fields, f"字段词典重复: {field}", errors)
        seen_fields.add(field)

        for key in ("category", "meaning"):
            require(isinstance(item.get(key), str) and item.get(key), f"{field} 缺少字符串字段: {key}", errors)

        for key in ("common_units", "notes"):
            require(isinstance(item.get(key), list), f"{field} 字段必须是列表: {key}", errors)
    return errors


def validate_runtime_interfaces(interface_names: list[str], strict: bool) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    try:
        import akshare as ak  # type: ignore
    except Exception as exc:
        warnings.append(f"未安装或无法导入 akshare，跳过运行时校验: {exc}")
        return errors, warnings

    for name in interface_names:
        if not hasattr(ak, name):
            message = f"akshare 中不存在接口: {name}"
            if strict:
                errors.append(message)
            else:
                warnings.append(message)
            continue
        try:
            inspect.signature(getattr(ak, name))
        except Exception as exc:
            warnings.append(f"无法读取接口签名 {name}: {exc}")
    return errors, warnings


def validate_docs_structure() -> list[str]:
    errors: list[str] = []
    for relative_path, headings in DOC_EXPECTATIONS.items():
        doc_path = ROOT / relative_path
        require(doc_path.exists(), f"缺少文档: {relative_path}", errors)
        if not doc_path.exists():
            continue
        content = doc_path.read_text(encoding="utf-8")
        for heading in headings:
            require(heading in content, f"{relative_path} 缺少章节: {heading}", errors)
    return errors


INTERFACE_HEADER_RE = re.compile(r"^###\s+([a-z0-9_]+(?:\s*/\s*[a-z0-9_]+)*)\s*$")


def extract_doc_interfaces(content: str) -> set[str]:
    interfaces: set[str] = set()
    for line in content.splitlines():
        match = INTERFACE_HEADER_RE.match(line.strip())
        if not match:
            continue
        for item in match.group(1).split("/"):
            interfaces.add(item.strip())
    return interfaces


def validate_doc_interface_coverage(known_interfaces: set[str]) -> list[str]:
    errors: list[str] = []
    for relative_path in DOC_EXPECTATIONS:
        doc_path = ROOT / relative_path
        if not doc_path.exists():
            continue
        for interface_name in sorted(extract_doc_interfaces(load_text(doc_path))):
            require(interface_name in known_interfaces, f"{relative_path} 中的接口未登记到 catalog: {interface_name}", errors)
    return errors


def validate_forbidden_text() -> list[str]:
    errors: list[str] = []
    for file_path in FORBIDDEN_SCAN_FILES:
        require(file_path.exists(), f"缺少文件: {file_path.relative_to(ROOT)}", errors)
        if not file_path.exists():
            continue
        content = load_text(file_path)
        for text in FORBIDDEN_TEXT:
            require(text not in content, f"{file_path.relative_to(ROOT)} 包含禁词或禁用引用: {text}", errors)
    return errors


def validate_source_policy() -> list[str]:
    errors: list[str] = []
    require(EXPECTED_SELECTION_POLICY in load_text(ROOT / "SKILL.md"), "SKILL.md 缺少非东方财富优先规则", errors)

    task_data = load_json(TASK_PLAYBOOKS)
    require(EXPECTED_SELECTION_POLICY in str(task_data.get("selection_policy", "")), "task_playbooks.json 缺少非东方财富优先规则", errors)

    interface_data = load_json(INTERFACE_CATALOG)
    require(EXPECTED_SELECTION_POLICY in str(interface_data.get("selection_policy", "")), "interface_catalog.json 缺少非东方财富优先规则", errors)

    for relative_path in DOC_EXPECTATIONS:
        content = load_text(ROOT / relative_path)
        require(EXPECTED_SELECTION_POLICY in content, f"{relative_path} 缺少非东方财富优先规则", errors)
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate AKShare skill registries.")
    parser.add_argument("--strict-interfaces", action="store_true", help="将运行时缺失接口视为错误而不是警告。")
    args = parser.parse_args()

    task_data = load_json(TASK_PLAYBOOKS)
    interface_data = load_json(INTERFACE_CATALOG)
    symbol_data = load_json(SYMBOL_FORMATS)
    glossary_data = load_json(FIELD_GLOSSARY)

    structural_errors: list[str] = []
    structural_warnings: list[str] = []

    interface_errors, interface_warnings = validate_interface_catalog(interface_data)
    structural_errors.extend(interface_errors)
    structural_warnings.extend(interface_warnings)

    interface_names = [item["function"] for item in interface_data.get("interfaces", []) if isinstance(item, dict) and item.get("function")]
    known_interfaces = set(interface_names)
    structural_errors.extend(validate_playbooks(task_data, known_interfaces))
    structural_errors.extend(validate_symbol_formats(symbol_data, known_interfaces))
    structural_errors.extend(validate_field_glossary(glossary_data))
    structural_errors.extend(validate_docs_structure())
    structural_errors.extend(validate_doc_interface_coverage(known_interfaces))
    structural_errors.extend(validate_forbidden_text())
    structural_errors.extend(validate_source_policy())

    runtime_errors, runtime_warnings = validate_runtime_interfaces(interface_names, strict=args.strict_interfaces)

    print("== 结构化校验结果 ==")
    print(f"playbooks: {len(task_data.get('playbooks', []))}")
    print(f"interfaces: {len(interface_names)}")
    print(f"symbol_formats: {len(symbol_data.get('formats', []))}")
    print(f"field_glossary: {len(glossary_data.get('fields', []))}")

    if structural_warnings:
        print("\n[WARN]")
        for item in structural_warnings:
            print(f"- {item}")

    if runtime_warnings:
        print("\n[WARN-RUNTIME]")
        for item in runtime_warnings:
            print(f"- {item}")

    all_errors = structural_errors + runtime_errors
    if all_errors:
        print("\n[ERROR]")
        for item in all_errors:
            print(f"- {item}")
        return 1

    print("\n校验通过")
    return 0


if __name__ == "__main__":
    sys.exit(main())

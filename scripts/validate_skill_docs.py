#!/usr/bin/env python3
"""Validate AKShare skill registries and optional runtime interface availability."""

from __future__ import annotations

import argparse
import inspect
import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
TASK_PLAYBOOKS = ROOT / "registry" / "task_playbooks.json"
INTERFACE_CATALOG = ROOT / "registry" / "interface_catalog.json"
DOC_EXPECTATIONS = {
    "docs/stock.md": ["## 任务路由", "## 高频接口", "## 结论输出建议", "## 常见坑"],
    "docs/fund.md": ["## 任务路由", "## 高频接口", "## 结论输出建议", "## 常见坑"],
    "docs/macro.md": ["## 任务路由", "## 高频接口", "## 结论输出建议", "## 常见坑"],
    "docs/news_sentiment.md": ["## 任务路由", "## 高频接口", "## 结论输出建议", "## 常见坑"],
    "docs/technical_analysis.md": ["## 任务路由", "## 高频指标", "## 结论输出建议", "## 常见坑"],
    "docs/fundamental_analysis.md": ["## 任务路由", "## 高频接口", "## 结论输出建议", "## 常见坑"],
}


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def require(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


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

        for key in ("aliases", "required_dimensions", "preferred_docs", "primary_interfaces", "output_sections"):
            value = item.get(key)
            require(isinstance(value, list) and value, f"{task_type} 缺少非空字段: {key}", errors)

        for doc_path in item.get("preferred_docs", []):
            require((ROOT / doc_path).exists(), f"{task_type} 引用了不存在的文档: {doc_path}", errors)

        for interface_name in item.get("primary_interfaces", []) + item.get("fallback_interfaces", []):
            require(
                interface_name in known_interfaces,
                f"{task_type} 引用了未登记接口: {interface_name}",
                errors,
            )
    return errors


def validate_interface_catalog(data: dict[str, Any]) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    interfaces = data.get("interfaces")
    require(
        isinstance(interfaces, list) and interfaces,
        "interface_catalog.json 缺少非空 interfaces 列表",
        errors,
    )
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


def validate_runtime_interfaces(interface_names: list[str], strict: bool) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    try:
        import akshare as ak  # type: ignore
    except Exception as exc:  # pragma: no cover - runtime dependent
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
        obj = getattr(ak, name)
        try:
            inspect.signature(obj)
        except Exception as exc:  # pragma: no cover - runtime dependent
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


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate AKShare skill registries.")
    parser.add_argument(
        "--strict-interfaces",
        action="store_true",
        help="将运行时缺失接口视为错误而不是警告。",
    )
    args = parser.parse_args()

    structural_errors: list[str] = []
    structural_warnings: list[str] = []

    task_data = load_json(TASK_PLAYBOOKS)
    interface_data = load_json(INTERFACE_CATALOG)

    interface_errors, interface_warnings = validate_interface_catalog(interface_data)
    structural_errors.extend(interface_errors)
    structural_warnings.extend(interface_warnings)

    interface_names = [item["function"] for item in interface_data.get("interfaces", []) if isinstance(item, dict) and item.get("function")]
    known_interfaces = set(interface_names)
    playbook_errors = validate_playbooks(task_data, known_interfaces)
    structural_errors.extend(playbook_errors)
    structural_errors.extend(validate_docs_structure())

    runtime_errors, runtime_warnings = validate_runtime_interfaces(interface_names, strict=args.strict_interfaces)

    print("== 结构化校验结果 ==")
    print(f"playbooks: {len(task_data.get('playbooks', []))}")
    print(f"interfaces: {len(interface_names)}")

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

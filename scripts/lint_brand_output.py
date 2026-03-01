#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOKENS = ROOT / "tokens" / "brand-tokens.json"


def fail(errors: list[str]) -> int:
    print("FAIL: output lint failed")
    for err in errors:
        print(f"- {err}")
    return 1


def extract_metadata(text: str) -> dict[str, str]:
    metadata: dict[str, str] = {}
    for line in text.splitlines():
        m = re.match(r"^\s*[-*]?\s*([a-z_]+):\s*(.+?)\s*$", line)
        if m:
            metadata[m.group(1)] = m.group(2)
    return metadata


def main() -> int:
    parser = argparse.ArgumentParser(description="Lint generated markdown for AIC brand compliance.")
    parser.add_argument("file", help="Path to markdown output file")
    parser.add_argument("--channel", choices=["remotion", "slides", "documents"], required=True)
    args = parser.parse_args()

    data = json.loads(TOKENS.read_text())
    path = Path(args.file)
    text = path.read_text()
    errors: list[str] = []

    metadata = extract_metadata(text)
    required_metadata = [
        "brand_package_version",
        "token_version",
        "runtime_independent",
        "local_assets_used",
        "font_substitution",
        "inferred_values_used",
        "contrast_check_passed",
        "channel",
    ]
    for key in required_metadata:
        if key not in metadata:
            errors.append(f"missing metadata key: {key}")

    if metadata.get("channel") and metadata["channel"] != args.channel:
        errors.append(f"channel mismatch: expected {args.channel}, got {metadata['channel']}")

    if "http://" in text or "https://" in text:
        errors.append("external URL detected in output (runtime output must be local-first)")

    approved = data["voice"]["approved_phrases"]
    if not any(phrase in text for phrase in approved):
        errors.append("none of the approved voice anchor phrases were used")

    discouraged = data["voice"]["discouraged_patterns"]
    for pattern in discouraged:
        if pattern in text:
            errors.append(f"discouraged voice pattern used: {pattern}")

    # Headings should generally be concise.
    for line in text.splitlines():
        if line.startswith("#"):
            heading = line.lstrip("#").strip()
            words = heading.split()
            if words and (len(words) < 3 or len(words) > 12):
                errors.append(f"heading word count out of bounds (3-12): '{heading}'")

    # Simple line length guardrail.
    for i, line in enumerate(text.splitlines(), start=1):
        if len(line) > 110:
            errors.append(f"line {i} exceeds 110 chars")

    if errors:
        return fail(errors)

    print("OK: output lint passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

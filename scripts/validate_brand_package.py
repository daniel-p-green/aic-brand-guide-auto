#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

from jsonschema import ValidationError, validate

ROOT = Path(__file__).resolve().parents[1]
TOKENS_PATH = ROOT / "tokens" / "brand-tokens.json"
SCHEMA_PATH = ROOT / "tokens" / "brand-tokens.schema.json"


def fail(msg: str) -> None:
    print(f"FAIL: {msg}")
    raise SystemExit(1)


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def hex_to_rgb(hex_color: str) -> tuple[float, float, float]:
    s = hex_color.lstrip("#")
    if len(s) != 6:
        fail(f"invalid hex color: {hex_color}")
    r = int(s[0:2], 16) / 255
    g = int(s[2:4], 16) / 255
    b = int(s[4:6], 16) / 255
    return r, g, b


def linearize(channel: float) -> float:
    return channel / 12.92 if channel <= 0.03928 else ((channel + 0.055) / 1.055) ** 2.4


def relative_luminance(hex_color: str) -> float:
    r, g, b = hex_to_rgb(hex_color)
    rl = linearize(r)
    gl = linearize(g)
    bl = linearize(b)
    return 0.2126 * rl + 0.7152 * gl + 0.0722 * bl


def contrast_ratio(fg: str, bg: str) -> float:
    l1 = relative_luminance(fg)
    l2 = relative_luminance(bg)
    lighter, darker = (l1, l2) if l1 >= l2 else (l2, l1)
    return (lighter + 0.05) / (darker + 0.05)


def require_contains(path: Path, phrases: list[str]) -> None:
    text = path.read_text()
    missing = [p for p in phrases if p not in text]
    if missing:
        fail(f"{path.relative_to(ROOT)} missing required phrases: {missing}")


def validate_examples() -> None:
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
    for rel in [
        "examples/slides-outline-template.md",
        "examples/document-template.md",
    ]:
        p = ROOT / rel
        text = p.read_text()
        for key in required_metadata:
            if key not in text:
                fail(f"{rel} missing metadata field: {key}")


def main() -> int:
    data = json.loads(TOKENS_PATH.read_text())
    schema = json.loads(SCHEMA_PATH.read_text())

    try:
        validate(instance=data, schema=schema)
    except ValidationError as e:
        fail(f"schema validation failed: {e.message}")

    if data["meta"].get("runtime_independent") is not True:
        fail("meta.runtime_independent must be true")

    # Logo integrity checks.
    for name, item in data["logos"].items():
        local = ROOT / item["local_path"]
        if not local.exists():
            fail(f"logo file missing: {name} -> {local}")
        if item.get("sha256") and sha256_file(local) != item["sha256"]:
            fail(f"logo checksum mismatch: {name}")

    # Font integrity checks.
    delivery = data["typography"]["delivery"]
    for font in delivery["local_files"]:
        p = ROOT / font["path"]
        if not p.exists():
            fail(f"font file missing: {font['path']}")
        if sha256_file(p) != font["sha256"]:
            fail(f"font checksum mismatch: {font['path']}")

    for lic in delivery["license_files"]:
        p = ROOT / lic["path"]
        if not p.exists():
            fail(f"license file missing: {lic['path']}")
        if sha256_file(p) != lic["sha256"]:
            fail(f"license checksum mismatch: {lic['path']}")

    # Typographic role sanity.
    roles = data["typography_scale"]["roles"]
    for role_name, role in roles.items():
        for bp in ["mobile", "tablet", "desktop"]:
            if role["size_px"][bp] <= 0:
                fail(f"{role_name} size must be > 0 at {bp}")

    # Required package files.
    required_files = [
        "brand.md",
        "ai-style-guide.md",
        "tokens/brand-theme.css",
        "tokens/brand-tokens.schema.json",
        "assets/brand-assets.md",
        "assets/fonts/README.md",
        "assets/fonts/LICENSES.md",
        "prompts/codex-brand-prompt.md",
        "prompts/claude-brand-prompt.md",
        "prompts/remotion-brand-prompt.md",
        "prompts/slides-brand-prompt.md",
        "prompts/document-brand-prompt.md",
        "remotion/scene-system.md",
        "slides/slide-system.md",
        "documents/document-system.md",
        "examples/slides-outline-template.md",
        "examples/document-template.md",
        "evidence/source-map.md",
    ]
    for rel in required_files:
        if not (ROOT / rel).exists():
            fail(f"missing required file: {rel}")

    # Cross-file phrase and channel consistency.
    approved_phrases = data["voice"]["approved_phrases"]
    require_contains(ROOT / "brand.md", approved_phrases)
    require_contains(ROOT / "ai-style-guide.md", ["remotion", "slides", "documents"])

    corpus = "\n".join(
        (ROOT / rel).read_text()
        for rel in [
            "brand.md",
            "ai-style-guide.md",
            "prompts/codex-brand-prompt.md",
            "prompts/claude-brand-prompt.md",
            "prompts/remotion-brand-prompt.md",
            "prompts/slides-brand-prompt.md",
            "prompts/document-brand-prompt.md",
        ]
    )
    for phrase in approved_phrases:
        if phrase not in corpus:
            fail(f"approved phrase missing from package corpus: {phrase}")

    # WCAG 2.2 AA contrast checks.
    light = data["colors"]["theme"]["light"]
    dark = data["colors"]["theme"]["dark"]
    orange = data["colors"]["core"]["aic_orange"]["hex"]
    black = data["colors"]["core"]["black"]["hex"]

    checks = [
        ("light body", light["foreground"]["hex"], light["background"]["hex"], 4.5),
        ("dark body", dark["foreground"]["hex"], dark["background"]["hex"], 4.5),
        ("orange CTA", black, orange, 4.5),
    ]
    for label, fg, bg, minimum in checks:
        ratio = contrast_ratio(fg, bg)
        if ratio < minimum:
            fail(f"contrast check failed ({label}): {ratio:.2f} < {minimum}")

    css_text = (ROOT / "tokens/brand-theme.css").read_text()
    if "--aic-cta-fg: #0c0a09;" not in css_text:
        fail("tokens/brand-theme.css must pin dark CTA foreground for AA contrast")

    validate_examples()

    print("OK: package validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

# AI-Ready Style Guide (Independent Package)

Version: 2.1.0

## Core Rule

Use this package as a closed system. Do not rely on live website values at runtime.

## 1) Required Local Inputs

- `tokens/brand-tokens.json`
- `tokens/brand-theme.css`
- `assets/logos/*.svg`
- `assets/fonts/**/*`

## 2) Mandatory Token Reads

Always load these token sections before generation:
- `logos`
- `colors`
- `typography`
- `typography_scale`
- `layout_scale`
- `formatting`
- `voice`
- `motion`
- `remotion`
- `slides`
- `documents`

## 3) Typography and Formatting Enforcement

- Map text to roles from `typography_scale.roles` only.
- Keep family binding (`serif` or `sans`) from each role.
- Apply heading, body, CTA, punctuation, and line-length rules from `formatting`.
- Apply channel-specific text limits from `remotion`, `slides`, or `documents`.

## 4) Color and Contrast Enforcement

- Resolve theme first (`light` or `dark`).
- Use only token-defined theme colors for surfaces and text.
- Use orange ramp for emphasis and primary CTA only.
- Reject outputs that fail WCAG 2.2 AA for body and CTA text.

## 5) Logo Enforcement

- Select white logo variants on dark/photo-heavy backgrounds.
- Select color variants on light backgrounds.
- Enforce minimum size and no-distortion policy.

## 6) Channel Routing

- Remotion outputs must also follow `remotion/scene-system.md`.
- Slide outputs must also follow `slides/slide-system.md`.
- Document outputs must also follow `documents/document-system.md`.

## 7) Failure Handling

If required tokens are missing:
1. Return `incomplete-token-state`.
2. List missing keys.
3. Stop generation.

If required local font files fail integrity checks:
1. Return `font-integrity-failed`.
2. List invalid files.
3. Stop generation.

## 8) Required Output Metadata

Include this block in generated outputs:
- `brand_package_version`
- `token_version`
- `runtime_independent`
- `local_assets_used`
- `font_substitution`
- `inferred_values_used`
- `contrast_check_passed`
- `channel` (`remotion` | `slides` | `documents`)

## 9) On-Brand QA Rubric

Score 1-5 per category. Minimum score: 36/45.

- Local runtime compliance
- Typography role compliance
- Formatting rule compliance
- Color and contrast compliance
- Logo usage compliance
- Voice compliance
- Channel-system compliance
- Accessibility compliance
- Motion/transition restraint

Reject output if any category is 2 or below.

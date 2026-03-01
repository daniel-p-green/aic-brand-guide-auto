# AI Collective Independent Brand Package

Local-first brand system for generating on-brand assets with AI agents and production tooling.

This repository is the runtime source for:
- Remotion videos
- Slide decks
- Documents
- Agent-generated branded outputs

## What This Includes

- Canonical human brand spec: `brand.md`
- Agent orchestration and QA rules: `ai-style-guide.md`
- Machine-readable tokens and schema:
  - `tokens/brand-tokens.json`
  - `tokens/brand-tokens.schema.json`
  - `tokens/brand-theme.css`
- Prompt modules for agent workflows:
  - `prompts/codex-brand-prompt.md`
  - `prompts/claude-brand-prompt.md`
  - `prompts/remotion-brand-prompt.md`
  - `prompts/slides-brand-prompt.md`
  - `prompts/document-brand-prompt.md`
- Channel systems:
  - `remotion/scene-system.md`
  - `slides/slide-system.md`
  - `documents/document-system.md`
- Local assets:
  - Logos in `assets/logos/`
  - Fonts in `assets/fonts/`
- Validation and lint tooling:
  - `scripts/validate_brand_package.py`
  - `scripts/lint_brand_output.py`

## Core Contract

- Runtime must be local-first and independent of live website requests.
- Generation must resolve values from local tokens and local assets.
- Outputs must pass contrast, typography, formatting, and channel-system checks.

## Quick Start

1. Validate the package:

```bash
python3 scripts/validate_brand_package.py
```

2. Choose a channel and use the matching prompt module:

- Remotion: `prompts/remotion-brand-prompt.md`
- Slides: `prompts/slides-brand-prompt.md`
- Documents: `prompts/document-brand-prompt.md`

3. Lint generated markdown outputs:

```bash
python3 scripts/lint_brand_output.py <file.md> --channel remotion
python3 scripts/lint_brand_output.py <file.md> --channel slides
python3 scripts/lint_brand_output.py <file.md> --channel documents
```

## Agent Usage Pattern

For Codex or Claude workflows:

1. Load `tokens/brand-tokens.json`.
2. Load the relevant prompt module from `prompts/`.
3. Load the channel system file (`remotion/`, `slides/`, or `documents/`).
4. Generate output with required metadata fields.
5. Run `lint_brand_output.py` and resolve any failures.

## Fonts

The package includes local runtime fonts:
- Georgia Pro (client-provided licensed files)
- Open Sans
- Source Serif 4

See:
- `assets/fonts/README.md`
- `assets/fonts/LICENSES.md`

## Legal and Brand Rights

Read `NOTICE.md` before public or commercial use.

## Evidence and Change Control

Evidence map and provenance:
- `evidence/source-map.md`
- `evidence/captures/`

If live public brand signals change, update evidence first, then tokens and prompts.

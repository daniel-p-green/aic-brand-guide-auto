# The AI Collective Brand Guide

Version: 2.1.0  
Package mode: Runtime independent (local-first)  
Evidence date: 2026-02-28  
Evidence map: `evidence/source-map.md`

## 1) Scope

This package is the canonical style system for:
- Remotion videos
- Slide decks
- Documents
- Agent-generated brand assets

All outputs must run from local package files only.

## 2) Runtime Independence Contract [Verified]

- Runtime source of truth: `tokens/brand-tokens.json`
- Runtime CSS classes: `tokens/brand-theme.css`
- Local logos: `assets/logos/*.svg`
- Local fonts and licenses: `assets/fonts/**/*`
- Do not fetch runtime style values from website endpoints.

## 3) Positioning and Voice [Verified]

The AI Collective communicates a people-centered AI movement that builds the human layer for the AI era through a global community of builders and stakeholders.

### Approved anchor phrases
- human layer
- AI era
- global community
- builders and stakeholders
- navigate technological progress

### Avoid
- fear-first AI framing
- unsupported superlatives
- exclusionary language
- buzzword-heavy filler

## 4) Logo System [Verified + Operational]

### Canonical files
- `assets/logos/logo.svg`
- `assets/logos/logo-white.svg`
- `assets/logos/wordmark.svg`
- `assets/logos/wordmark-white.svg`

### Usage rules
- Do not stretch, crop, skew, or recolor logos.
- Use white variants on dark/photo-heavy backgrounds.
- Use color variants on light/neutral backgrounds.
- Minimum widths: mark 24px, wordmark 120px.
- Clearspace defaults are operational values in `tokens.brand-tokens.json`.

## 5) Color Guide

### Core brand colors [Verified]
- AIC Orange: `#ff640d`
- Wordmark Slate: `#374151`
- White: `#ffffff`
- Near Black: `#0c0a09`

### Theme values [Verified]
- Light: background `#f5f5f4`, foreground `#292524`, accent `#ebebea`
- Dark: background `#0c0a09`, foreground `#f5f5f4`, accent `#3b3835`

### Color rules [Operational]
- Use orange for emphasis and primary CTA only.
- Keep neutral tones dominant.
- Ensure WCAG 2.2 AA contrast for body text and CTA labels.

## 6) Font Guide

### Families
- Serif primary: Georgia Pro (licensed, client-provided local files included)
- Serif fallback: Source Serif 4 (bundled)
- Sans primary: Open Sans (bundled)

### Runtime policy
- Load fonts from `assets/fonts` only.
- If Georgia Pro is unavailable, map all serif roles to Source Serif 4.
- Preserve token-defined sizes, line-height, and letter-spacing during substitution.

## 7) Text Sizing and Scaling

Use `typography_scale.roles` as strict style roles.

### Role summary (mobile/tablet/desktop px)
- Display: 44/60/84
- H1: 34/48/64
- H2: 28/36/48
- H3: 24/30/40
- H4: 20/24/30
- Body L: 18/19/20
- Body: 16/17/18
- Body S: 14/15/16
- Label: 12/13/14
- Caption: 11/12/13

## 8) Formatting Instructions

### Headings
- 3-12 words preferred.
- Use title case for major headings.
- Avoid end punctuation unless required.

### Body
- Target 45-75 characters per line.
- One idea per paragraph.

### CTA
- 2-5 words.
- Start with an action verb.

## 9) Layout Rules

- Base spacing unit: 4px
- Spacing scale: 4, 8, 12, 16, 24, 32, 48, 64, 96
- Radius scale: 6, 10, 16, 24
- Container max width: 1280px
- Grid: 12 columns
- Safe zone defaults: top 8%, bottom 12%, sides 6%

## 10) Channel Systems

### Remotion
Use:
- `remotion/scene-system.md`
- `prompts/remotion-brand-prompt.md`
- `tokens.remotion`

### Slides
Use:
- `slides/slide-system.md`
- `prompts/slides-brand-prompt.md`
- `tokens.slides`

### Documents
Use:
- `documents/document-system.md`
- `prompts/document-brand-prompt.md`
- `tokens.documents`

## 11) Unknowns (Explicit)

- No publicly discovered official clearspace formula from brand owners.
- No publicly discovered official print/Pantone guide.
- No publicly discovered official published motion handbook.

Operational defaults are included and labeled as operational.

# AI-Ready Style Guide for Codex, Claude, and Remotion

Version: 1.0.0  
Token source of truth: `tokens/brand-tokens.json`  
Evidence source: `evidence/source-map.md`
Public-use notice: `NOTICE.md`

## 1) System Objective
Generate on-brand assets that reflect AI Collective's human-centered, globally coordinated AI narrative while preserving visual consistency and accessibility.

## 2) Token Binding Rules
All generation systems must read values from token keys before producing output.

### Required token bindings
- Brand identity:
  - `meta.brand_name`
- Logo decisions:
  - `logos.logo`
  - `logos.logo_white`
  - `logos.wordmark`
  - `logos.wordmark_white`
- Theme palette:
  - `color.light`
  - `color.dark`
  - `color.brand`
- Type system:
  - `typography.heading_family`
  - `typography.body_family`
- Voice constraints:
  - `voice.approved_phrases`
  - `voice.discouraged_patterns`
- Motion and video defaults:
  - `motion.*`
  - `remotion.*`

If a required token is missing, fail safely: emit an `incomplete-token-state` warning and do not fabricate hard values.

## 3) Generation Constraints

### Canonical voice phrase set (must remain exact across guides/prompts)
- human layer
- AI era
- global community
- builders and stakeholders
- navigate technological progress

### Visual constraints
- Use serif-led title hierarchy and sans-led support text.
- Maintain orange accent as the primary energy color (`color.brand.primary_hex`).
- Match light/dark backgrounds to the corresponding token groups.
- Preserve logo aspect ratios and approved variant/background pairing.

### Copy constraints
- Reinforce human/community framing and practical collaboration.
- Use concise sentence structure and avoid inflated speculative language.
- Include at least one approved phrase when context allows, without forced repetition.

### Structural constraints
- Prefer clear narrative flow:
  - Context
  - Value
  - Invitation/CTA
- Keep CTA text direct and actionable.

## 4) Fallback Rules for Unknowns
Unknowns are explicit in this package. When encountering an unknown:
1. State uncertainty in output metadata.
2. Use inferred operational defaults only if labeled as inference-compatible.
3. Avoid claiming inferred values as official brand policy.

## 5) Channel-Specific Prompt Scaffolds
Use the files below as the primary runtime prompts:
- `prompts/codex-brand-prompt.md`
- `prompts/claude-brand-prompt.md`
- `prompts/remotion-brand-prompt.md`

## 6) Quality Gates
Every generated asset should be checked against this gate sequence:
1. Token compliance: all required keys resolved.
2. Logo compliance: correct variant and no distortion.
3. Typography compliance: heading/body family use.
4. Color compliance: background/foreground contrast and brand accent consistency.
5. Voice compliance: no discouraged patterns.
6. Accessibility compliance: WCAG 2.2 AA target contrast.
7. Rights check: intended logo/trademark use has explicit permission for destination channel.

## 7) Output Metadata Contract
Attach this metadata block in pipeline output (JSON or frontmatter):
- `brand_package_version`
- `token_version`
- `evidence_snapshot_date`
- `confidence_level` (high/medium/low)
- `inferred_values_used` (array)
- `accessibility_check_status`
- `rights_review_status`

## 8) On-Brand QA Rubric
Score each category 1-5; minimum accepted aggregate is 28/40.

- Brand fidelity: reflects AI Collective purpose and tone.
- Token fidelity: values map directly to token file.
- Logo correctness: variant/background pairing and no unauthorized edits.
- Typography hierarchy: serif/sans usage aligns with system.
- Color harmony: neutral + orange energy balance is preserved.
- Motion appropriateness: tasteful, readable, and not distracting.
- Copy clarity: concise, credible, and action-oriented.
- Accessibility: contrast and readability meet target standards.

If any category scores 2 or below, reject and regenerate.

# Codex Brand Prompt Module (AI Collective)

## Input Expectations
- Target asset type and channel (web/social/video/slide).
- Target theme (`light` or `dark`).
- Audience and outcome.
- Available token file: `tokens/brand-tokens.json`.

## Generation Constraints
- Canonical approved phrase set (must remain exact):
  - human layer
  - AI era
  - global community
  - builders and stakeholders
  - navigate technological progress
- Read token values before generating output.
- Use approved brand voice and avoid discouraged patterns.
- Use serif-led headings and sans-led utility/body text.
- Select logo variant based on background:
  - Dark background -> white logo/wordmark variants.
  - Light background -> default color variants.
- Preserve logo vector proportions and avoid visual effects on marks.
- Keep design atmosphere editorial + modern, with restrained grain/gradient ambience.

## Quality Checklist
- [ ] Required token keys resolved.
- [ ] Logo variant is correct for background.
- [ ] Heading/body typography mapping follows tokens.
- [ ] Copy includes at least one approved phrase where natural.
- [ ] No discouraged language patterns.
- [ ] Contrast appears WCAG 2.2 AA-safe.
- [ ] Output metadata includes inference disclosure if any inferred token used.

## Failure Handling
If a required token is missing or contradictory:
1. Stop generation.
2. Return `incomplete-token-state` with missing keys.
3. Provide a minimal remediation list.

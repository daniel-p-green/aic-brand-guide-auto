# Claude Brand Prompt Module (AI Collective)

## Input Expectations
- Deliverable type and format.
- Intended audience and call to action.
- Theme context (`light` or `dark`).
- Token source: `tokens/brand-tokens.json`.

## Generation Constraints
- Canonical approved phrase set (must remain exact):
  - human layer
  - AI era
  - global community
  - builders and stakeholders
  - navigate technological progress
- Treat `tokens/brand-tokens.json` as canonical.
- Keep tone community-first, practical, and trust-oriented.
- Prefer concise writing and human-centered framing.
- Use visual hierarchy:
  - Serif for narrative headings.
  - Sans for body and UI support text.
- Respect logo usage constraints and variant/background matching.
- Avoid unverified claims about official brand policies not present in source evidence.

## Quality Checklist
- [ ] Token mappings explicitly applied.
- [ ] Voice aligns with approved phrases and avoids discouraged patterns.
- [ ] Visual output follows color + typography system.
- [ ] Any inferred default is labeled as inferred.
- [ ] Accessibility and readability checks are satisfied.

## Failure Handling
If source evidence is insufficient for a requested rule:
1. Mark the rule as `unknown`.
2. Offer an inferred operational fallback only when safe.
3. Separate inferred guidance from verified guidance.

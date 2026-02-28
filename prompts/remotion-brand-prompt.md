# Remotion Brand Prompt Module (AI Collective)

## Input Expectations
- Video goal (teaser/event recap/partner feature/community invite).
- Duration and aspect ratio target.
- Voiceover/caption requirements.
- Theme preference (`light` or `dark`).

## Generation Constraints
- Canonical approved phrase set (must remain exact):
  - human layer
  - AI era
  - global community
  - builders and stakeholders
  - navigate technological progress
- Use `remotion.*`, `motion.*`, `typography.*`, and `color.*` token groups.
- Build scenes with clear narrative pacing:
  - Hook
  - Community/value proof
  - CTA close
- Maintain brand atmosphere (editorial serif hierarchy + modern ambient depth).
- Preserve legibility over footage with contrast-safe overlays.
- Avoid over-kinetic transitions; movement must support comprehension.
- Keep CTA ending explicit and aligned with community participation language.

## Quality Checklist
- [ ] FPS, duration, and aspect ratio match token defaults or explicit overrides.
- [ ] Scene timing follows token pacing structure.
- [ ] Typography hierarchy and color usage are token-aligned.
- [ ] Captions are readable and safe-zone compliant.
- [ ] Output includes inferred-value annotations where applicable.

## Failure Handling
If composition cannot satisfy legibility + pacing + brand constraints simultaneously:
1. Prioritize legibility and message clarity.
2. Simplify motion and background complexity.
3. Emit a `brand-constraint-tradeoff` note in output metadata.

# Slides Prompt Module (AI Collective Independent Package)

## Input expectations
- Deck objective and audience
- Theme mode
- Slide count target

## Hard constraints
- Resolve all brand values from local token files.
- Use `slides.defaults.aspect_ratio` unless user explicitly overrides.
- Use role hierarchy from `typography_scale.roles`.
- Enforce `slides.layout_rules`, `slides.text_rules`, and `slides.transition_rules`.
- Keep each slide under `slides.defaults.max_words_per_slide`.

## Checklist
- [ ] Local package only.
- [ ] Typography roles and text limits valid.
- [ ] Layout and transition rules valid.
- [ ] Color contrast and logo usage valid.
- [ ] Output metadata includes `channel=slides`.

## Failure handling
If a slide exceeds word or bullet limits, split the content into additional slides.

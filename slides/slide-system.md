# AI Collective Slide System (Independent)

Token source: `tokens/brand-tokens.json`  
Theme classes: `tokens/brand-theme.css`

## Slide grammar
- S0 Title and promise
- S1 Context
- S2 Problem
- S3 Insight
- S4 Proof
- S5 Next step CTA

## Type role mapping
- Title slide: `display` or `h1`
- Section headers: `h2` or `h3`
- Bullet body: `body` or `body_s`
- Metadata: `label` or `caption`

## Content limits
- Max bullets per slide: 5
- Max words per slide: 55
- One core idea per slide

## Layout rules
- Maintain at least 7% margin on all sides.
- Keep title zone in top third.
- Place logo only once per slide.

## Transition rules
- Allowed: dissolve, fade, simple push.
- Transition duration: 300ms to 500ms.
- Avoid stacking effects on one element.

## Formatting map
- Headings follow `formatting.heading_rules`.
- Body follows `formatting.body_rules`.
- CTA follows `formatting.cta_rules`.

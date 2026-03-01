# AI Collective Remotion Scene System (Independent)

Token source: `tokens/brand-tokens.json`  
Theme classes: `tokens/brand-theme.css`

## Scene grammar
- S0 Hook (0-4s)
- S1 Context (4-12s)
- S2 Proof (12-24s)
- S3 CTA (24-30s)

## Type role mapping
- Hook headline: `display` or `h1`
- Section heading: `h2`/`h3`
- Body overlays: `body`/`body_s`
- Metadata and chips: `label`/`caption`

## Formatting map
- Heading text follows `formatting.heading_rules`
- Body text follows `formatting.body_rules`
- CTA text follows `formatting.cta_rules`

## Motion map
- micro interactions: 180ms
- standard transitions: 420ms
- hero transitions: 800ms

Use restrained transitions and maintain text readability at all times.

## Asset rules
- Use only local logo files from `assets/logos`.
- White logos for dark scenes, color logos for light scenes.
- Never distort vector aspect ratio.

## Safe-zone defaults
- Top 8%
- Bottom 12%
- Sides 6%

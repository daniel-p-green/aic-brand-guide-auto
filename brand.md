# The AI Collective Brand Guide

Version: 1.0.0  
Evidence date: 2026-02-28  
Primary evidence map: `evidence/source-map.md`
Public-use/legal notice: `NOTICE.md`

## Brand Purpose [Verified]
The AI Collective is positioned as a people-centered AI organization that is building the human layer for the AI era. Public copy repeatedly emphasizes global community coordination, practical forums, and trust-building among builders, stakeholders, and leaders. (Evidence: E-002, E-003, E-026)

## Positioning Statement [Verified]
The brand presents itself as the world's largest AI community, uniting 200k+ pioneers across 100+ global chapters, with messaging oriented around helping society navigate accelerating technological progress. (Evidence: E-002)

## Brand Pillars [Verified]
- Community at scale: global chapter network and recurring gatherings. (Evidence: E-002, E-026)
- Human coordination: conversations, forums, and stakeholder alignment. (Evidence: E-003, E-026)
- Practical progress: builders and operators sharing real frontier signals. (Evidence: E-024, E-026)
- Responsible momentum: trust and participation over hype. (Evidence: E-003, E-026)

## Visual DNA [Inference]
The live visual system combines editorial serif hierarchy with atmospheric, modern interfaces:
- Serif-forward narrative headings.
- High-contrast composition and dark-mode confidence.
- Grain and gradient ambience to create depth.
- Warm orange energy accents against cool neutrals and deep backgrounds.

This section is marked inference because explicit public prose describing visual philosophy is not published; it is derived from observed implementation patterns.
Primary evidence basis: E-021, E-023, E-025.

## Logo System

### Approved Assets [Verified]
- `https://www.aicollective.com/images/brand/Logo.svg` (Evidence: E-004, E-005)
- `https://www.aicollective.com/images/brand/Logo-White.svg` (Evidence: E-006)
- `https://www.aicollective.com/images/brand/Wordmark.svg` (Evidence: E-007, E-008)
- `https://www.aicollective.com/images/brand/Wordmark-White.svg` (Evidence: E-009)

### Core Logo Specs [Verified]
- Logo mark viewBox: `0 0 700 844.38` (Evidence: E-004)
- Wordmark viewBox: `0 0 1290.68 620.57` (Evidence: E-007)
- Logo brand fill: `#ff640d` (Evidence: E-005)
- Wordmark text fill (light variant): `#374151` (Evidence: E-008)

### Usage Rules [Inference]
- Use white variants on dark/photographic backgrounds where standard variants fail contrast.
- Use colored variants on light or neutral backgrounds.
- Preserve intrinsic aspect ratio; do not stretch logos.
- Avoid applying shadows, gradients, strokes, or filters directly to logo paths.

Primary evidence basis: E-006, E-009, E-022.

### Unknowns (Explicit) [Verified]
- No public clearspace/min-size specification is discovered. (Unknown: U-001)
- No public official lockup spacing formula is discovered. (Unknown: U-002)

## Color System

### Authoritative Tokens from Live CSS [Verified]
Evidence group: E-010, E-011, E-012, E-013, E-014, E-015, E-016, E-017.
- Light:
  - `--background: 60 5% 96%`
  - `--foreground: 12 6% 15%`
  - `--primary: 12 6% 15%`
  - `--accent: 60 4% 92%`
- Dark:
  - `--background: 20 14% 4%`
  - `--foreground: 60 5% 96%`
  - `--primary: 60 5% 96%`
  - `--accent: 30 6% 22%`

### Signature Brand Colors [Verified]
- AIC Orange: `#ff640d` (Evidence: E-005)
- Wordmark Slate: `#374151` (Evidence: E-008)

### Operational Semantic Colors [Inference]
For generated assets where status semantics are needed (success/warning/error/info), use the semantic tokens in `tokens/brand-tokens.json` and mark output as operational/inferred when applicable.

## Typography

### Typeface System [Verified]
- Primary sans: `Open Sans` (Evidence: E-019)
- Primary serif: `georgiaPro` (Evidence: E-020)
- Heading pattern: observed serif application for major headings (`h1`, `h2`, `h3`). (Evidence: E-021)

### Typographic Intent [Inference]
- Serif for narrative authority and editorial character.
- Sans for utility text, metadata, and dense content readability.
- Maintain strong contrast between hero/headline and support copy.

Primary evidence basis: E-019, E-020, E-021.

## Imagery and Composition

### Observed Patterns [Verified]
- Community event photography is central to storytelling. (Evidence: E-026)
- Background treatments include textured grain and gradient haze. (Evidence: E-023)
- Section blocks often juxtapose human portraits or gatherings with concise explanatory copy. (Evidence: E-023, E-026)

### Generation Guidance [Inference]
- Prefer real-world collaborative scenes over abstract AI iconography.
- Use ambient overlays subtly; avoid overpowering the subject.
- Keep CTAs visually clear and color-differentiated.

Primary evidence basis: E-023, E-024, E-026.

## Voice and Messaging

### Core Voice [Verified]
- People-forward, trust-oriented, globally inclusive, and action-oriented.
- Language emphasizes forums, collaboration, and responsible coordination.

Evidence group: E-002, E-003, E-026.

### Voice Anchors [Verified]
Use and reinforce phrases such as:
- human layer
- AI era
- global community
- builders and stakeholders
- navigate technological progress

Evidence group: E-002, E-003.

### Voice Guardrails [Inference]
- Do not use fear-first framing or speculative doom language.
- Avoid empty superlatives without concrete grounding.
- Prefer clear, concise, credible language over buzzword-heavy copy.

Primary evidence basis: E-003, E-024, E-026.

## Motion Principles

### Observed Technical Signals [Verified]
The live CSS includes extensive motion tokens and spring/easing variables, suggesting deliberate animated interaction patterns. (Evidence: E-025)

### Operational Motion Rules [Inference]
- Prioritize legibility and hierarchy over novelty.
- Use smooth transitions with restrained timing.
- Honor reduced-motion user preferences.

Primary evidence basis: E-025.

## Accessibility Requirements

### Required [Inference]
- Maintain WCAG 2.2 AA text contrast for all generated assets.
- Ensure CTA labels and body copy remain readable over image/video backgrounds.
- Provide reduced-motion alternatives for motion-heavy deliverables.

Rationale: accessibility requirements are implementation standards for generation workflows; explicit brand accessibility documentation was not discovered publicly.
Primary evidence basis: E-022 and observed tokenized theme structure (E-010 to E-017).

## Anti-Patterns

### Do Not [Inference]
- Distort, recolor, or stylize logo vectors beyond approved variants.
- Replace editorial typography with generic, overly geometric defaults.
- Overload layouts with excessive visual effects.
- Use copy that frames AI progress as detached from people.

Primary evidence basis: E-003, E-005, E-006, E-008, E-009.

## Cross-Reference Index
- Machine-readable tokens: `tokens/brand-tokens.json`
- Token schema: `tokens/brand-tokens.schema.json`
- Agent orchestration: `ai-style-guide.md`
- Remotion scene grammar: `remotion/scene-system.md`
- Source traceability: `evidence/source-map.md`

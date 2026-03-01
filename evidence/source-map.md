# AI Collective Brand Evidence Source Map

Snapshot date: 2026-02-28
Method: Live-source capture from public AI Collective web assets and stylesheets.
Confidence scale: High (direct literal), Medium (strongly implied by multiple direct literals), Low (inference for operational use).

| Evidence ID | Topic | Value / Observation | Source URL | Captured On | Confidence | Notes |
|---|---|---|---|---|---|---|
| E-001 | Brand name | `The AI Collective` | https://www.aicollective.com | 2026-02-28 | High | Present in `<title>` and metadata. |
| E-002 | Primary message | `The world's largest AI community. Uniting 200k+ pioneers across 100+ global chapters. Building the human layer for the AI era.` | https://www.aicollective.com | 2026-02-28 | High | Meta description + structured data. |
| E-003 | Voice anchors | `human layer`, `AI era`, `global community`, `chapters`, `builders`, `stakeholders` | https://www.aicollective.com | 2026-02-28 | High | Repeated in hero/about sections. |
| E-004 | Logo mark viewBox | `0 0 700 844.38` | https://www.aicollective.com/images/brand/Logo.svg | 2026-02-28 | High | Direct SVG attribute. |
| E-005 | Logo mark brand color | `#ff640d` | https://www.aicollective.com/images/brand/Logo.svg | 2026-02-28 | High | SVG `.cls-1,.cls-2{fill:#ff640d;}`. |
| E-006 | Logo white variant | White fills (`#fff`) | https://www.aicollective.com/images/brand/Logo-White.svg | 2026-02-28 | High | SVG `.cls-1,.cls-2{fill:#fff;}`. |
| E-007 | Wordmark viewBox | `0 0 1290.68 620.57` | https://www.aicollective.com/images/brand/Wordmark.svg | 2026-02-28 | High | Direct SVG attribute. |
| E-008 | Wordmark text color | `#374151` | https://www.aicollective.com/images/brand/Wordmark.svg | 2026-02-28 | High | SVG `.cls-3{fill:#374151;}`. |
| E-009 | Wordmark white variant | White fills (`#fff`) | https://www.aicollective.com/images/brand/Wordmark-White.svg | 2026-02-28 | High | White-safe wordmark variant. |
| E-010 | Light background token | `--background: 60 5% 96%` | https://www.aicollective.com/_next/static/css/5cccc2448d0e2390.css | 2026-02-28 | High | Direct root token. Build-hash asset; see `evidence/captures/2026-02-28-css-token-extracts.md` and refresh procedure below. |
| E-011 | Light foreground token | `--foreground: 12 6% 15%` | https://www.aicollective.com/_next/static/css/5cccc2448d0e2390.css | 2026-02-28 | High | Direct root token. Build-hash asset; see capture file. |
| E-012 | Light primary token | `--primary: 12 6% 15%` | https://www.aicollective.com/_next/static/css/5cccc2448d0e2390.css | 2026-02-28 | High | Direct root token. Build-hash asset; see capture file. |
| E-013 | Light accent token | `--accent: 60 4% 92%` | https://www.aicollective.com/_next/static/css/5cccc2448d0e2390.css | 2026-02-28 | High | Direct root token. Build-hash asset; see capture file. |
| E-014 | Dark background token | `--background: 20 14% 4%` | https://www.aicollective.com/_next/static/css/5cccc2448d0e2390.css | 2026-02-28 | High | Direct `.dark` token. Build-hash asset; see capture file. |
| E-015 | Dark foreground token | `--foreground: 60 5% 96%` | https://www.aicollective.com/_next/static/css/5cccc2448d0e2390.css | 2026-02-28 | High | Direct `.dark` token. Build-hash asset; see capture file. |
| E-016 | Dark primary token | `--primary: 60 5% 96%` | https://www.aicollective.com/_next/static/css/5cccc2448d0e2390.css | 2026-02-28 | High | Direct `.dark` token. Build-hash asset; see capture file. |
| E-017 | Dark accent token | `--accent: 30 6% 22%` | https://www.aicollective.com/_next/static/css/5cccc2448d0e2390.css | 2026-02-28 | High | Direct `.dark` token. Build-hash asset; see capture file. |
| E-018 | Border radius token | `--radius: 1rem` | https://www.aicollective.com/_next/static/css/5cccc2448d0e2390.css | 2026-02-28 | High | Root token used broadly. Build-hash asset; see capture file. |
| E-019 | Sans family | `Open Sans` | https://www.aicollective.com/_next/static/css/2d1ac66977c42890.css | 2026-02-28 | High | Font-face + token var. Build-hash asset; see capture file. |
| E-020 | Serif family | `georgiaPro` | https://www.aicollective.com/_next/static/css/2d1ac66977c42890.css | 2026-02-28 | High | Font-face + token var. Build-hash asset; see capture file. |
| E-021 | Heading style pattern | Headings use serif (`h1,h2,h3` mapped to Georgia Pro stack) | https://www.aicollective.com/_next/static/css/5cccc2448d0e2390.css | 2026-02-28 | High | Direct CSS selector. Build-hash asset; see capture file. |
| E-022 | Theme meta colors | Light theme-color `#f5f5f4`, dark `#0c0a09` | https://www.aicollective.com | 2026-02-28 | High | Direct meta tags. |
| E-023 | Visual motif | Grain/gradient atmospheric background layer | https://www.aicollective.com | 2026-02-28 | Medium | Observable in rendered homepage and `GrainientBackground` component naming. |
| E-024 | CTA tone | `Join The Collective`, `Find An Event`, `Learn More` | https://www.aicollective.com | 2026-02-28 | High | Direct UI labels. |
| E-025 | Motion style hint | Motion utility presets + spring variables in CSS | https://www.aicollective.com/_next/static/css/5cccc2448d0e2390.css | 2026-02-28 | Medium | Direct token presence; exact authored rationale inferred. |
| E-026 | Community-first framing | `forums worldwide`, `conversations among peers`, `stakeholders` | https://www.aicollective.com | 2026-02-28 | High | Hero/about/community copy. |
| E-027 | Open Sans licensing baseline | SIL OFL package for Open Sans is publicly distributable | https://github.com/google/fonts/tree/main/ofl/opensans | 2026-02-28 | High | Used for local runtime font bundling and offline operation. |
| E-028 | Source Serif 4 licensing baseline | SIL OFL package for Source Serif 4 is publicly distributable | https://github.com/google/fonts/tree/main/ofl/sourceserif4 | 2026-02-28 | High | Used as local serif fallback when Georgia Pro is unavailable. |
| E-029 | CTA contrast enforcement | `#0c0a09` on `#ff640d` exceeds WCAG AA (6.66:1) while white does not | local calculation from token colors | 2026-02-28 | High | Enforced in package validator and theme token `--aic-cta-fg`. |
| E-030 | Georgia Pro local availability | Georgia regular/italic/bold/bold-italic files available in local AI Collective font folder | local path: `/Users/danielgreen/Library/Mobile Documents/com~apple~CloudDocs/AI Collective/Fonts` | 2026-02-28 | High | Used as local licensed primary serif in this package. |

## Unknowns (Explicitly Not Invented)

- U-001: Formal logo clearspace ratio and minimum size rules are not published in discovered public assets.  
- U-002: Official lockup spacing formulas are not present in discovered public sources.  
- U-003: Official print CMYK values and Pantone mappings are not present in discovered public sources.  
- U-004: Official licensed photo treatment rules (beyond observed style) are not provided in discovered public sources.  
- U-005: Official motion duration/easing specs for brand exports are not published as a dedicated motion brand guide.

These are represented in deliverables with explicit `unknown` or `inferred` flags.

## Refresh Procedure for Build-Hashed CSS Sources

1. Open `https://www.aicollective.com` and identify active CSS bundles under `/_next/static/css/`.
2. Resolve the latest CSS files that contain target tokens/fonts (`--background`, `--foreground`, `Open Sans`, `georgiaPro`, `h1,h2,h3` selectors).
3. Update evidence rows E-010 to E-021 with the new hash URLs and append a dated capture file in `evidence/captures/`.

# AI Collective Asset Manifest

Snapshot date: 2026-02-28

## Officially Discovered Public Brand SVG Assets

| Asset ID | URL | Variant Type | ViewBox | Approx Aspect Ratio | Primary Fill | Intended Background | Status |
|---|---|---|---|---:|---|---|---|
| A-LOGO-COLOR | https://www.aicollective.com/images/brand/Logo.svg | Mark color | `0 0 700 844.38` | 0.828997 | `#ff640d` | Light / neutral | Verified |
| A-LOGO-WHITE | https://www.aicollective.com/images/brand/Logo-White.svg | Mark white | `0 0 700 844.38` | 0.828997 | `#ffffff` | Dark / image-rich | Verified |
| A-WORDMARK-COLOR | https://www.aicollective.com/images/brand/Wordmark.svg | Wordmark color | `0 0 1290.68 620.57` | 2.079881 | `#374151` (text), `#ff640d` (mark) | Light / neutral | Verified |
| A-WORDMARK-WHITE | https://www.aicollective.com/images/brand/Wordmark-White.svg | Wordmark white | `0 0 1290.68 620.57` | 2.079881 | `#ffffff` | Dark / image-rich | Verified |

## Usage Guidance
- Use color variants when background luminance is high enough for contrast.
- Use white variants when backgrounds are dark, busy, or photo/video-heavy.
- Keep logos unmodified:
  - no stretch,
  - no recolor,
  - no bevel/shadow/filter effects on vector paths.

## Approved Contrast Contexts (Operational)

### Prefer color logo when
- Background is near light token background (`color.light.background`).
- Foreground complexity behind logo is minimal.

### Prefer white logo when
- Background maps to dark token background (`color.dark.background`).
- Logo appears over dynamic photo/video overlays.

## Source and Integrity Notes
- All entries above are direct URLs discovered from public AI Collective site assets.
- No checksums are included in this package yet; treat this as a live URL manifest.
- Public use requires legal/trademark review; see `NOTICE.md`.

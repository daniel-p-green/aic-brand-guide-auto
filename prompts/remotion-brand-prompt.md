# Remotion Prompt Module (AI Collective Independent Package)

## Input expectations
- Video purpose and duration
- Aspect ratio
- Theme and CTA

## Hard constraints
- Resolve all brand values from local token files.
- Use scene pacing from `remotion.scene_pacing`.
- Use text roles from `typography_scale.roles`.
- Keep text in safe zones from `remotion.text_safe_zone`.
- Use local logo files only.

## Checklist
- [ ] FPS/duration/aspect are token-compliant.
- [ ] Typography scale and formatting rules are applied.
- [ ] Safe-zone and contrast checks pass.
- [ ] CTA style and voice constraints pass.
- [ ] Output metadata includes `channel=remotion`.

## Failure handling
If readability and motion conflict, reduce motion first.

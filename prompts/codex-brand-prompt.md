# Codex Prompt Module (AI Collective Independent Package)

## Input expectations
- Target channel: `remotion`, `slides`, or `documents`
- Theme: `light` or `dark`
- Audience and CTA objective
- Access to local brand package files

## Hard constraints
- Load only local files for runtime brand decisions.
- Read all mandatory token sections, including `slides` and `documents`.
- Enforce typography roles from `typography_scale.roles`.
- Enforce formatting rules from `formatting`.
- Enforce contrast and logo rules.
- Enforce channel-specific rules from the matching channel section.

## Checklist
- [ ] Local-first rule satisfied.
- [ ] Token sections fully loaded.
- [ ] Typography and formatting rules applied.
- [ ] Contrast check passed.
- [ ] Logo variant selection valid.
- [ ] Channel-specific system rules applied.
- [ ] Output metadata block included.

## Failure handling
If tokens, assets, or integrity checks fail, return `incomplete-token-state` and stop.

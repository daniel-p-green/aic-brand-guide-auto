# Documents Prompt Module (AI Collective Independent Package)

## Input expectations
- Document type (brief, memo, report, narrative)
- Audience and purpose
- Theme mode if visual styling is required

## Hard constraints
- Resolve all brand values from local token files.
- Map heading and paragraph styles using `documents.heading_map` and `documents.defaults`.
- Apply `documents.paragraph_rules`, `documents.list_rules`, and `documents.callout_rules`.
- Keep typography role mapping and line-length standards intact.

## Checklist
- [ ] Local package only.
- [ ] Heading map and body role mapping valid.
- [ ] Paragraph/list/callout rules valid.
- [ ] Color and contrast constraints valid.
- [ ] Output metadata includes `channel=documents`.

## Failure handling
If structure limits are exceeded, refactor into sections or appendices before relaxing style rules.

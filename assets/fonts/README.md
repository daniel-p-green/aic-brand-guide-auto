# Local Font Provisioning (Runtime Independent)

This package runs without fetching fonts from `aicollective.com` or any remote font CDN at runtime.

## Included Font Files

The repository includes local runtime fonts:

- `assets/fonts/georgia-pro/GeorgiaPro-Regular.ttf`
- `assets/fonts/georgia-pro/GeorgiaPro-Italic.ttf`
- `assets/fonts/georgia-pro/GeorgiaPro-Bold.ttf`
- `assets/fonts/georgia-pro/GeorgiaPro-BoldItalic.ttf`
- `assets/fonts/open-sans/OpenSans-VariableFont_wdth,wght.ttf`
- `assets/fonts/open-sans/OpenSans-Italic-VariableFont_wdth,wght.ttf`
- `assets/fonts/source-serif-4/SourceSerif4-VariableFont_opsz,wght.ttf`
- `assets/fonts/source-serif-4/SourceSerif4-Italic-VariableFont_opsz,wght.ttf`

## Required Families

- Sans primary: Open Sans (included)
- Serif primary: Georgia Pro (licensed, included from client-provided files)
- Serif fallback: Source Serif 4 (included)

## Georgia Pro Notes

Georgia Pro files are included for this repository and should remain internal to licensed usage.
If you need to refresh or replace them, use this path:

```text
assets/fonts/georgia-pro/
  GeorgiaPro-Regular.ttf
  GeorgiaPro-Italic.ttf
  GeorgiaPro-Bold.ttf
  GeorgiaPro-BoldItalic.ttf
```

If Georgia Pro is unavailable in another environment, the package must use Source Serif 4 for every serif role.

## Runtime Policy

1. Load fonts from local paths only.
2. Do not fetch runtime fonts from websites or external font APIs.
3. Use Open Sans for sans roles.
4. Use Georgia Pro for serif roles by default.
5. Keep role sizing and line-height values unchanged during substitution.
6. When serif semibold is needed and no semibold cut exists, map semibold to Georgia bold.

## Integrity and Licensing

- Font file checksums are pinned in `tokens/brand-tokens.json`.
- License text files are bundled under each open-source family folder.
- See `assets/fonts/LICENSES.md` for provenance and license summary.

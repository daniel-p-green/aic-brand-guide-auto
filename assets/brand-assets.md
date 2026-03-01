# Brand Asset Manifest (Local Runtime Package)

All runtime usage should reference local files.

## Local logo files

| Asset | Local Path | SHA-256 | ViewBox | Min Width |
|---|---|---|---|---:|
| Logo Color | `assets/logos/logo.svg` | `c55675f916cf424df1041018c4b64b4b1d8aea17ce50ff8818cc9baeeab76a0b` | `0 0 700 844.38` | 24px |
| Logo White | `assets/logos/logo-white.svg` | `150aaa600736de7b09885e17f04916eac5ecdececda1f008ad3d7235d8f1b9a0` | `0 0 700 844.38` | 24px |
| Wordmark Color | `assets/logos/wordmark.svg` | `665ad302cb7fdb10e9d7269dc225f79930c9cc91ea9f9b550a37471f8a63311f` | `0 0 1290.68 620.57` | 120px |
| Wordmark White | `assets/logos/wordmark-white.svg` | `3ee3173a0d14741a4b021ea095b84edaf21b27e4a5b9303418a061bf3922f136` | `0 0 1290.68 620.57` | 120px |

## Local font files

| Family | Style | Local Path | SHA-256 |
|---|---|---|---|
| Georgia Pro | Regular | `assets/fonts/georgia-pro/GeorgiaPro-Regular.ttf` | `4f54eb299fccea7f103edeb0d92437359bfd4441811d53222b82b335369f6218` |
| Georgia Pro | Italic | `assets/fonts/georgia-pro/GeorgiaPro-Italic.ttf` | `7758840cacb7382db65aa038e9fd1194d077ba9b55fe748f9cfb196d2773ac4e` |
| Georgia Pro | Bold | `assets/fonts/georgia-pro/GeorgiaPro-Bold.ttf` | `1cfa9abd55be746c798c22ef4eba88fce82257934897404be2dae53ed0a4142a` |
| Georgia Pro | Bold Italic | `assets/fonts/georgia-pro/GeorgiaPro-BoldItalic.ttf` | `a2036878f47d0da1765869a8747cfb0079b6125776675bad352468b59ca4493d` |
| Open Sans | Normal | `assets/fonts/open-sans/OpenSans-VariableFont_wdth,wght.ttf` | `36643644f318a812aab2d2ed3bb98f8cf0872527f835fe9398d95fe6b9adb878` |
| Open Sans | Italic | `assets/fonts/open-sans/OpenSans-Italic-VariableFont_wdth,wght.ttf` | `fe269381e992f32e135801740998544d6235061e37c93ec067ad2be3edd5b17b` |
| Source Serif 4 | Normal | `assets/fonts/source-serif-4/SourceSerif4-VariableFont_opsz,wght.ttf` | `97b2d4da6e3cb494b5a1e66ae176914d852ccabef49e0c02c0df25f3e39aca0b` |
| Source Serif 4 | Italic | `assets/fonts/source-serif-4/SourceSerif4-Italic-VariableFont_opsz,wght.ttf` | `15fbc7e4679489a501998c3669272637a6646388ef7e4bd77eebb5bf967a1f42` |

## Font licensing

- Open Sans and Source Serif 4 use SIL Open Font License 1.1.
- Local license files are included at:
  - `assets/fonts/open-sans/OFL.txt`
  - `assets/fonts/source-serif-4/OFL.txt`
- Georgia Pro files are client-provided licensed assets for internal use.

## Runtime usage policy

- Local paths are authoritative at runtime.
- Source URLs are provenance only and not required during generation.
- Agents must fail closed if required local asset checksums do not match token values.

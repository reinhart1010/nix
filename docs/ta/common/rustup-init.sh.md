---
layout: page
title: common/rustup-init.sh (தமிழ்)
description: "`rustup` மற்றும் ரஸ்ட் கருவித்தொகுப்பை நிறுவுவதற்கான ஸ்கிரிப்ட்."
content_hash: a6ace6abe9edb9d62407c4068f89e98a0aa18ac5
last_modified_at: 2023-06-24
related_topics:
  - title: English version
    url: /en/common/rustup-init.sh.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># rustup-init.sh

`rustup` மற்றும் ரஸ்ட் கருவித்தொகுப்பை நிறுவுவதற்கான ஸ்கிரிப்ட்.
மேலும் விவரத்திற்கு: <https://forge.rust-lang.org/infra/other-installation-methods.html#rustup>.

- `rustup` மற்றும் இயல்புநிலை ரஸ்ட் கருவித்தொகுப்பை நிறுவ, `rustup-init` ஐப் பதிவிறக்கி இயக்கவும்:

`curl https://sh.rustup.rs -sSf | sh -s`

- பதிவிறக்கி, `rustup-init` ஐ இயக்கி, அதற்கு வாதங்களை அனுப்பவும்:

`curl https://sh.rustup.rs -sSf | sh -s -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">வாதங்கள்</span>

- `rustup-init` ஐ இயக்கி, நிறுவுவதற்கான கூடுதல் கூறுகள் அல்லது இலக்குகளைக் குறிப்பிடவும்:

`rustup-init.sh --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">இலக்கு</span>` --component `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கூறு</span>

- `rustup-init` ஐ இயக்கி, நிறுவ வேண்டிய இயல்புநிலை கருவித்தொகுப்பைக் குறிப்பிடவும்:

`rustup-init.sh --default-toolchain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கருவித்தொகுப்பு</span>

- `rustup-init` ஐ இயக்கவும் மற்றும் எந்த கருவித்தொகுப்பையும் நிறுவ வேண்டாம்:

`rustup-init.sh --default-toolchain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">none</span>

- `rustup-init` ஐ இயக்கி, நிறுவல் சுயவிவரத்தைக் குறிப்பிடவும்:

`rustup-init.sh --profile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">minimal|default|complete</span>

- உறுதிப்படுத்தலைக் கேட்காமல் `rustup-init` ஐ இயக்கவும்:

`rustup-init.sh -y`

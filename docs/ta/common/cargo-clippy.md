---
layout: page
title: common/cargo-clippy (தமிழ்)
description: "பொதுவான தவறுகளைப் பிடிக்கவும் உங்கள் ரஸ்ட் குறியீட்டை மேம்படுத்தவும் லிண்ட்களின் தொகுப்பு."
content_hash: 73b0bde9fe6e081126cf31ce71b441a4595721dc
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/cargo-clippy.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/cargo-clippy.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cargo clippy

பொதுவான தவறுகளைப் பிடிக்கவும் உங்கள் ரஸ்ட் குறியீட்டை மேம்படுத்தவும் லிண்ட்களின் தொகுப்பு.
மேலும் விவரத்திற்கு: <https://github.com/rust-lang/rust-clippy>.

- தற்போதைய கோப்பகத்தில் உள்ள குறியீட்டின் மீது காசோலைகளை இயக்கவும்:

`cargo clippy`

- `Cargo.lock` புதுப்பித்த நிலையில் இருக்க வேண்டும்:

`cargo clippy --locked`

- பணியிடத்தில் உள்ள அனைத்து தொகுப்புகளிலும் சரிபார்ப்புகளை இயக்கவும்:

`cargo clippy --workspace`

- தொகுப்புக்கான காசோலைகளை இயக்கவும்:

`cargo clippy --package `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">தொகுப்பு</span>

- எச்சரிக்கைகளை பிழைகளாகக் கருதுங்கள்:

`cargo clippy -- --deny warnings`

- சோதனைகளை இயக்கவும் மற்றும் எச்சரிக்கைகளை புறக்கணிக்கவும்:

`cargo clippy -- --allow warnings`

- Clippy பரிந்துரைகளை தானாகவே பயன்படுத்தவும்:

`cargo clippy --fix`

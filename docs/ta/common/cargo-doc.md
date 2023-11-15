---
layout: page
title: common/cargo-doc (தமிழ்)
description: "ரஸ்ட் தொகுப்புகளின் ஆவணங்களை உருவாக்கவும்."
content_hash: b10395dfb8e6869bc60705ab7bdafd0a0a4b670b
last_modified_at: 2023-11-15
related_topics:
  - title: English version
    url: /en/common/cargo-doc.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/cargo-doc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cargo doc

ரஸ்ட் தொகுப்புகளின் ஆவணங்களை உருவாக்கவும்.
மேலும் விவரத்திற்கு: <https://doc.rust-lang.org/cargo/commands/cargo-doc.html>.

- தற்போதைய திட்டம் மற்றும் அனைத்து சார்புகளுக்கான ஆவணங்களை உருவாக்கவும்:

`cargo doc`

- சார்புகளுக்கான ஆவணங்களை உருவாக்க வேண்டாம்:

`cargo doc --no-deps`

- உலாவியில் ஆவணங்களை உருவாக்கி திறக்கவும்:

`cargo doc --open`

- ஒரு குறிப்பிட்ட தொகுப்பின் ஆவணங்களை உருவாக்கி பார்க்கவும்:

`cargo doc --open --package `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">தொகுப்பு</span>

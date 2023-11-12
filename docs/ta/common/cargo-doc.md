---
layout: page
title: common/cargo-doc (தமிழ்)
description: "ரஸ்ட் தொகுப்பு ஆவணங்களை ஆஃப்லைனில் உருவாக்கி பார்க்கவும்."
content_hash: 6a6b970975e23f870774c40a9bf0d1e378a48049
last_modified_at: 2023-11-12
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

ரஸ்ட் தொகுப்பு ஆவணங்களை ஆஃப்லைனில் உருவாக்கி பார்க்கவும்.
மேலும் விவரத்திற்கு: <https://doc.rust-lang.org/cargo/commands/cargo-doc.html>.

- உலாவியில் இயல்புநிலை தொகுப்பு ஆவணங்களை உருவாக்கி பார்க்கவும்:

`cargo doc --open`

- பிணையத்தை அணுகாமல் ஆவணங்களை உருவாக்கவும்:

`cargo doc --offline`

- குறிப்பிட்ட தொகுப்பின் ஆவணங்களைப் பார்க்கவும்:

`cargo doc --open --package `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">தொகுப்பு</span>

- குறிப்பிட்ட தொகுப்பின் ஆவணங்களை ஆஃப்லைனில் பார்க்கவும்:

`cargo doc --open --offline --package `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">தொகுப்பு</span>

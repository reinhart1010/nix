---
layout: page
title: common/cargo-rustc (தமிழ்)
description: "ரஸ்ட் தொகுப்பைத் தொகுக்கவும். `cargo build` போன்றது, ஆனால் நீங்கள் கூடுதல் விருப்பங்களை கம்பைலருக்கு அனுப்பலாம்."
content_hash: a67bd2df64a259958361d1be2beedc6b22c14da3
last_modified_at: 2023-11-13
related_topics:
  - title: English version
    url: /en/common/cargo-rustc.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/cargo-rustc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cargo rustc

ரஸ்ட் தொகுப்பைத் தொகுக்கவும். `cargo build` போன்றது, ஆனால் நீங்கள் கூடுதல் விருப்பங்களை கம்பைலருக்கு அனுப்பலாம்.
கிடைக்கக்கூடிய அனைத்து விருப்பங்களுக்கு `rustc --help` ஐப் பார்க்கவும்.
மேலும் விவரத்திற்கு: <https://doc.rust-lang.org/cargo/commands/cargo-rustc.html>.

- தொகுப்பை உருவாக்கி விருப்பங்களை `rustc` க்கு அனுப்பவும்:

`cargo rustc -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rustc_options</span>

- மேம்படுத்தல்களுடன், வெளியீட்டு பயன்முறையில் கலைப்பொருட்களை உருவாக்கவும்:

`cargo rustc --release`

- தற்போதைய CPUக்கான கட்டமைப்பு-குறிப்பிட்ட மேம்படுத்தல்களுடன் தொகுக்கவும்:

`cargo rustc --release -- -C target-cpu=native`

- வேக உகப்பாக்கத்துடன் தொகுக்கவும்:

`cargo rustc -- -C opt-level `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1|2|3</span>

- [s]ize (அளவு) ஆப்டிமைசேஷன் மூலம் தொகுக்கவும் (`z` லூப் வெக்டரைசேஷனையும் முடக்குகிறது):

`cargo rustc -- -C opt-level `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">s|z</span>

- உங்கள் தொகுப்பு பாதுகாப்பற்ற குறியீட்டைப் பயன்படுத்துகிறதா எனச் சரிபார்க்கவும்:

`cargo rustc --lib -- -D unsafe-code`

- ஒரு குறிப்பிட்ட தொகுப்பை உருவாக்கவும்:

`cargo rustc --package `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">தொகுப்பு</span>

- குறிப்பிட்ட பைனரியை மட்டும் உருவாக்கவும்:

`cargo --bin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பெயர்</span>

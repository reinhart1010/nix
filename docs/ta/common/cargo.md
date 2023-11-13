---
layout: page
title: common/cargo (தமிழ்)
description: "ரஸ்ட் திட்டங்கள் மற்றும் அவற்றின் தொகுதி சார்புகளை (கிரேட்ஸ்) நிர்வகிக்கவும்."
content_hash: f64d6f244f1774c3e4dc2f26cbec4f6232b4137f
last_modified_at: 2023-11-13
related_topics:
  - title: Deutsch version
    url: /de/common/cargo.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/cargo.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/cargo.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/cargo.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/cargo.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/cargo.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/cargo.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/cargo.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cargo

ரஸ்ட் திட்டங்கள் மற்றும் அவற்றின் தொகுதி சார்புகளை (கிரேட்ஸ்) நிர்வகிக்கவும்.
`build` போன்ற சில துணைக் கட்டளைகள் அவற்றின் சொந்த பயன்பாட்டு ஆவணங்களைக் கொண்டுள்ளன.
மேலும் விவரத்திற்கு: <https://doc.rust-lang.org/cargo>.

- கிரேட்ஸைத் தேடுங்கள்:

`cargo search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">தேடல்_சரம்</span>

- ஒரு பைனரி பெட்டியை நிறுவவும்:

`cargo install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கிரேட்_பெயர்</span>

- நிறுவப்பட்ட பைனரி பெட்டிகளை பட்டியலிடுங்கள்:

`cargo install --list`

- குறிப்பிட்ட கோப்பகத்தில் புதிய பைனரி அல்லது நூலகம் ரஸ்ட் திட்டத்தை உருவாக்கவும் (அல்லது முன்னிருப்பாக தற்போதைய வேலை கோப்பகம்):

`cargo init --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bin|lib</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">அடைவிற்குப்/பாதை</span>

- தற்போதைய கோப்பகத்தில் `Cargo.toml` இல் சார்புநிலையைச் சேர்க்கவும்:

`cargo add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">சார்பு</span>

- வெளியீட்டு சுயவிவரத்தைப் பயன்படுத்தி தற்போதைய கோப்பகத்தில் ரஸ்ட் திட்டத்தை உருவாக்கவும்:

`cargo build --release`

- நைட்லி கம்பைலரைப் பயன்படுத்தி தற்போதைய கோப்பகத்தில் ரஸ்ட் திட்டத்தை உருவாக்கவும் (`rustup` தேவை):

`cargo +nightly build`

- குறிப்பிட்ட எண்ணிக்கையிலான நூல்களைப் பயன்படுத்தி உருவாக்கவும் (இயல்புநிலை தருக்க CPU கோர்களின் எண்ணிக்கை):

`cargo build --jobs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">நூல்களின்_எண்ணிக்கை</span>

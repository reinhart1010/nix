---
layout: page
title: common/cargo (தமிழ்)
description: "ரஸ்ட் திட்டங்கள் மற்றும் அவற்றின் தொகுதி சார்புகளை (கிரேட்ஸ்) நிர்வகிக்கவும்."
content_hash: e9ee5839bf0a395437ffce9c3c14c0965fb0e498
last_modified_at: 2022-12-03
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
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/cargo.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># cargo

ரஸ்ட் திட்டங்கள் மற்றும் அவற்றின் தொகுதி சார்புகளை (கிரேட்ஸ்) நிர்வகிக்கவும்.
`cargo build` போன்ற சில துணைக் கட்டளைகள் அவற்றின் சொந்த பயன்பாட்டு ஆவணங்களைக் கொண்டுள்ளன.
மேலும் விவரத்திற்கு: <https://crates.io>.

- கிரேட்ஸைத் தேடுங்கள்:

`cargo search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">தேடல்_சரம்</span>

- ஒரு பெட்டியை நிறுவவும்:

`cargo install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கிரேட்_பெயர்</span>

- நிறுவப்பட்ட பெட்டிகளை பட்டியலிடுங்கள்:

`cargo install --list`

- தற்போதைய கோப்பகத்தில் புதிய பைனரி அல்லது லைப்ரரி ரஸ்ட் திட்டத்தை உருவாக்கவும்:

`cargo init --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bin|lib</span>

- குறிப்பிட்ட கோப்பகத்தில் புதிய பைனரி அல்லது லைப்ரரி ரஸ்ட் திட்டத்தை உருவாக்கவும்:

`cargo new `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">அடைவிற்குப்/பாதை</span>` --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bin|lib</span>

- தற்போதைய கோப்பகத்தில் ரஸ்ட் திட்டத்தை உருவாக்கவும்:

`cargo build`

- நைட்லி கம்பைலரைப் பயன்படுத்தி தற்போதைய கோப்பகத்தில் ரஸ்ட் திட்டத்தை உருவாக்கவும்:

`cargo +nightly build`

- குறிப்பிட்ட எண்ணிக்கையிலான நூல்களைப் பயன்படுத்தி உருவாக்கவும் (இயல்புநிலை CPU கோர்களின் எண்ணிக்கை):

`cargo build --jobs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">நூல்களின்_எண்ணிக்கை</span>

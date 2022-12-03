---
layout: page
title: common/ab (தமிழ்)
description: "அப்பாச்சி HTTP சர்வர் தரப்படுத்தல் கருவி."
content_hash: a94e6a82c69ded62860060fc04e7f387f430b3c9
last_modified_at: 2022-12-03
related_topics:
  - title: Deutsch version
    url: /de/common/ab.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ab.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/ab.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ab.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/ab.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ab.html
    icon: bi bi-globe
  - title: norsk version
    url: /no/common/ab.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/ab.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/ab.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/ab.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ab.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ab

அப்பாச்சி HTTP சர்வர் தரப்படுத்தல் கருவி.
மேலும் விவரத்திற்கு: <https://httpd.apache.org/docs/current/programs/ab.html>.

- கொடுக்கப்பட்ட முகவரிக்கு 100 HTTP GET கோரிக்கைகளை இயக்கவும்:

`ab -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">முகவரி</span>

- 100 HTTP GET கோரிக்கைகளை, ஒரே நேரத்தில் 10 தொகுதிகளில், URL முகவரிக்கு செயல்படுத்தவும்:

`ab -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">முகவரி</span>

- ஒரு கோப்பிலிருந்து JSON பேலோடைப் பயன்படுத்தி, 100 HTTP POST கோரிக்கைகளை URL க்கு செயல்படுத்தவும்:

`ab -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">application/json</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/கோப்பு.json</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">முகவரி</span>

- HTTP [K]eep Alive ஐப் பயன்படுத்தவும், அதாவது ஒரு HTTP அமர்வுக்குள் பல கோரிக்கைகளைச் செய்யவும்:

`ab -k `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">முகவரி</span>

- தரப்படுத்தலுக்கு செலவிட வேண்டிய அதிகபட்ச வினாடிகளை அமைக்கவும்:

`ab -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">60</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">முகவரி</span>

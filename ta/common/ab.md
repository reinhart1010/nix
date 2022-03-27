---
layout: page
title: common/ab (தமிழ்)
description: "அப்பாச்சி தரப்படுத்தல் கருவி. சுமை சோதனை செய்ய எளிய கருவி."
content_hash: 920207a448970c994ae7b709300d27c1604e2982
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
  - title: norsk bokmål (Norge) version
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

அப்பாச்சி தரப்படுத்தல் கருவி. சுமை சோதனை செய்ய எளிய கருவி.
மேலும் விவரத்திற்கு: <https://httpd.apache.org/docs/current/programs/ab.html>.

- கொடுக்கப்பட்ட முகவரி க்கு 100 HTTP GET கோரிக்கைகளை இயக்கவும்:

`ab -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">முகவரி</span>

- கொடுக்கப்பட்ட முகவரி க்கு 100 HTTP GET கோரிக்கைகளை ஒரே நேரத்தில் 10 கோரிக்கைகள் வீதம் செயல்படுத்தவும்:

`ab -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">முகவரி</span>

- இணைப்பை தொடரச்செய்:

`ab -k `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">முகவரி</span>

- தரப்படுத்தல் குறிக்க செலவழிக்க அதிகபட்ச விநாடிகளை அமைக்கவும்:

`ab -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">60</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">முகவரி</span>

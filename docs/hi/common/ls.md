---
layout: page
title: common/ls (हिन्दी)
description: "निर्देशिका सामग्री को सूचीबद्ध करें।"
content_hash: fd4ed137d0eb2ec5c3a390d989443c0d2ec026f3
related_topics:
  - title: Deutsch version
    url: /de/common/ls.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ls.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/ls.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/ls.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ls.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/ls.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/ls.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/ls.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ls.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/ls.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/ls.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/ls.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/ls.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ls.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ls

निर्देशिका सामग्री को सूचीबद्ध करें।
अधिक जानकारी: <https://www.gnu.org/software/coreutils/ls>।

- प्रति पंक्ति एक फ़ाइल की सूची बनाएं:

`ls -1`

- छिपी हुई फाइलों सहित सभी फाइलों की सूची बनाएं:

`ls -a`

- सभी फाइलों को सूचीबद्ध करें, '/' के साथ निर्देशिका नामों को समाप्त करें:

`ls -F`

- सभी फ़ाइलों की लंबी प्रारूप सूची (अनुमतियाँ, स्वामित्व, आकार और परिवर्तन तिथि):

`ls -la`

- मानव पठनीय इकाइयों (KiB, MiB, GiB) का उपयोग करके प्रदर्शित आकार के साथ लंबी प्रारूप सूची:

`ls -lh`

- आकार के अनुसार क्रमबद्ध लंबी सूची (घटते हुए):

`ls -lS`

- संशोधन की तारीख (सबसे पहले) द्वारा क्रमबद्ध सभी फाइलों की लंबी प्रारूप सूची:

`ls -ltr`

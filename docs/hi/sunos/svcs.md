---
layout: page
title: sunos/svcs (हिन्दी)
description: "चल रहे सेवाओं के बारे में जानकारी सूचीबद्ध करें।"
content_hash: 4902526a2cf824ad18d71fdc9d1d2085413dd1c8
last_modified_at: 2024-10-30
related_topics:
  - title: English version
    url: /en/sunos/svcs.html
    icon: bi bi-globe
  - title: français version
    url: /fr/sunos/svcs.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/sunos/svcs.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/sunos/svcs.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/sunos/svcs.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/sunos/svcs.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/sunos/svcs.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/sunos/svcs.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/sunos/svcs.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># svcs

चल रहे सेवाओं के बारे में जानकारी सूचीबद्ध करें।
अधिक जानकारी: <https://www.unix.com/man-page/linux/1/svcs>।

- सभी चल रही सेवाओं की सूची बनाएं:

`svcs`

- उन सेवाओं की सूची बनाएं जो चल नहीं रही हैं:

`svcs -vx`

- किसी सेवा के बारे में जानकारी सूचीबद्ध करें:

`svcs apache`

- सेवा लॉग फ़ाइल के स्थान को दिखाएं:

`svcs -L apache`

- सेवा लॉग फ़ाइल के अंत को प्रदर्शित करें:

`tail $(svcs -L apache)`

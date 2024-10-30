---
layout: page
title: sunos/devfsadm (हिन्दी)
description: "`/dev` के लिए प्रशासनिक आदेश। `/dev` नामस्थान को बनाए रखता है।"
content_hash: 88e0420266d98ff7906b17498b578c16b2c8fa55
last_modified_at: 2024-10-30
related_topics:
  - title: English version
    url: /en/sunos/devfsadm.html
    icon: bi bi-globe
  - title: français version
    url: /fr/sunos/devfsadm.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/sunos/devfsadm.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/sunos/devfsadm.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/sunos/devfsadm.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/sunos/devfsadm.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/sunos/devfsadm.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/sunos/devfsadm.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/sunos/devfsadm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# devfsadm

`/dev` के लिए प्रशासनिक आदेश। `/dev` नामस्थान को बनाए रखता है।
अधिक जानकारी: <https://www.unix.com/man-page/sunos/1m/devfsadm>।

- नए डिस्क के लिए स्कैन करें:

`devfsadm -c disk`

- किसी भी लटके हुए /dev लिंक को साफ करें और नए उपकरण के लिए स्कैन करें:

`devfsadm -C -v`

- ड्राई-रन - यह आउटपुट करता है कि क्या बदला जाएगा लेकिन कोई संशोधन नहीं करता:

`devfsadm -C -v -n`

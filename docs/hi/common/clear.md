---
layout: page
title: common/clear (हिन्दी)
description: "टर्मिनल की स्क्रीन साफ़ करें।"
content_hash: 9fb262fc7994a70dfd3f788defdf124f14ce695d
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/clear.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/clear.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/clear.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/clear.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/clear.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/clear.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/clear.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/clear.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/clear.html
    icon: bi bi-globe
tldri18n_status: 2
---
# clear

टर्मिनल की स्क्रीन साफ़ करें।
अधिक जानकारी: <https://manned.org/clear>।

- स्क्रीन साफ़ करें (बैश शेल में Control-L दबाने के बराबर):

`clear`

- स्क्रीन साफ़ करें लेकिन टर्मिनल का स्क्रॉलबैक बफ़र रखें:

`clear -x`

- साफ करने के लिए टर्मिनल के प्रकार को इंगित करें (डिफॉल्ट रूप से एनवायरमेंट वेरिएबल `TERM` का मूल्य):

`clear -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">टर्मिनल_का_प्रकार</span>

- `ncurses` का संस्करण दिखाएं जिसका उपयोग `clear` द्वारा किया गया है:

`clear -V`

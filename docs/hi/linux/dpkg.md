---
layout: page
title: linux/dpkg (हिन्दी)
description: "डेबियन पैकेज प्रबंधक।"
content_hash: 2753a2a54fbb34daa72dbc970edd66c385f3df32
last_modified_at: 2024-10-15
related_topics:
  - title: Deutsch version
    url: /de/linux/dpkg.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/dpkg.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/dpkg.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/dpkg.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/dpkg.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># dpkg

डेबियन पैकेज प्रबंधक।
कुछ उपकमांड जैसे `dpkg deb` के अपने स्वयं के उपयोग दस्तावेज़ हैं।
अन्य पैकेज प्रबंधकों में समकक्ष कमांड के लिए, देखें <https://wiki.archlinux.org/title/Pacman/Rosetta>.
अधिक जानकारी: <https://manned.org/dpkg>।

- एक पैकेज इनस्टॉल करें:

`dpkg -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">फ़ाइल.deb/का/पथ</span>

- एक पैकेज निकालें:

`dpkg -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">पैकेज_का_नाम</span>

- इन्सटाल्ड पैकेजों की सूची बनाएं:

`dpkg -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">पैटर्न</span>

- पैकेज की सामग्री सूचीबद्ध करें:

`dpkg -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">पैकेज_का_नाम</span>

- लोकल पैकेज फ़ाइल की सामग्री सूचीबद्ध करें:

`dpkg -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">फ़ाइल.deb/का/पथ</span>

- पता लगाएं कि कौन सा पैकेज फ़ाइल का मालिक है:

`dpkg -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">फ़ाइल_का_नाम</span>

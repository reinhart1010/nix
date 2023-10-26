---
layout: page
title: linux/apk (हिन्दी)
description: "अल्पाइन लिनक्स पैकेज प्रबंधन उपकरण।"
content_hash: 2b6f4949b57f8fd86acef8dea1fd53f8e2c81142
last_modified_at: 2023-10-26
related_topics:
  - title: Deutsch version
    url: /de/linux/apk.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/apk.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/apk.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/apk.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/apk.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/apk.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/apk.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/apk.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/apk.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># apk

अल्पाइन लिनक्स पैकेज प्रबंधन उपकरण।
अधिक जानकारी: <https://wiki.alpinelinux.org/wiki/Alpine_Linux_package_management>.

- सभी दूरस्थ रिपॉजिटरी से रिपॉजिटरी इंडेक्स अपडेट करें:

`apk update`

- एक नया पैकेज स्थापित करें:

`apk add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">पैकेज</span>

- एक पैकेज निकालें:

`apk del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">पैकेज</span>

- किसी पैकेज की मरम्मत करें या मुख्य निर्भरता को संशोधित किए बिना उसे अपग्रेड करें:

`apk fix `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">पैकेज</span>

- कीवर्ड के माध्यम से पैकेज खोजें:

`apk search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">कीवर्ड</span>

- किसी विशिष्ट पैकेज के बारे में जानकारी प्रदर्शित करें:

`apk info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">पैकेज</span>

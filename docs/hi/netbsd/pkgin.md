---
layout: page
title: netbsd/pkgin (हिन्दी)
description: "NetBSD पर `pkgsrc` बाइनरी पैकेज प्रबंधित करें।"
content_hash: 68937b30c76dc07d7572ce81a31a0a45f56c6a3f
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/netbsd/pkgin.html
    icon: bi bi-globe
  - title: español version
    url: /es/netbsd/pkgin.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/netbsd/pkgin.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/netbsd/pkgin.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/netbsd/pkgin.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pkgin

NetBSD पर `pkgsrc` बाइनरी पैकेज प्रबंधित करें।
अधिक जानकारी: <https://pkgin.net/#usage>।

- एक पैकेज स्थापित करें:

`pkgin install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">पैकेज</span>

- एक पैकेज और उसकी निर्भरताएँ हटाएँ:

`pkgin remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">पैकेज</span>

- सभी पैकेज को उन्नत करें:

`pkgin full-upgrade`

- एक पैकेज के लिए खोजें:

`pkgin search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">कीवर्ड</span>

- स्थापित पैकेजों की सूची बनाएं:

`pkgin list`

- अनावश्यक निर्भरताएँ हटाएँ:

`pkgin autoremove`

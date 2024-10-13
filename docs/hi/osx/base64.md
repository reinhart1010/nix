---
layout: page
title: osx/base64 (हिन्दी)
description: "बेस 64 प्रस्तुतीकरण का उपयोग करके कोड और डिकोड करें।"
content_hash: e3bca8463f17863e86175ea8db9ecd00d2a1e065
last_modified_at: 2024-10-13
related_topics:
  - title: English version
    url: /en/osx/base64.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/base64.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/osx/base64.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/osx/base64.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/osx/base64.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/base64.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/base64.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># base64

बेस 64 प्रस्तुतीकरण का उपयोग करके कोड और डिकोड करें।
अधिक जानकारी: <https://keith.github.io/xcode-man-pages/base64.1.html>।

- फ़ाइल को कोड करें:

`base64 --input=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">सादा_फ़ाइल</span>

- फ़ाइल को डिकोड करें:

`base64 --decode --input=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">base64_फ़ाइल</span>

- `stdin` से कोड करें:

`echo -n "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">सादा_फ़ाइल</span>`" | base64`

- `stdin` से डिकोड करें:

`echo -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">base64_फ़ाइल</span>` | base64 --decode`

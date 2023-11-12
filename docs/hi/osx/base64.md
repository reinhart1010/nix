---
layout: page
title: osx/base64 (हिन्दी)
description: "बेस 64 प्रस्तुतीकरण का उपयोग करके कोड और डिकोड करें।"
content_hash: e82a2b2161aee16de3e422caee5a5822540aabd8
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/osx/base64.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/base64.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/osx/base64.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/base64.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/base64.html
    icon: bi bi-globe
tldri18n_status: 2
---
# base64

बेस 64 प्रस्तुतीकरण का उपयोग करके कोड और डिकोड करें।
अधिक जानकारी: <https://www.unix.com/man-page/osx/1/base64/>।

- फ़ाइल को कोड करें:

`base64 --input=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">सादा_फ़ाइल</span>

- फ़ाइल को डिकोड करें:

`base64 --decode --input=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">base64_फ़ाइल</span>

- `stdin` से कोड करें:

`echo -n "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">सादा_फ़ाइल</span>`" | base64`

- `stdin` से डिकोड करें:

`echo -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">base64_फ़ाइल</span>` | base64 --decode`

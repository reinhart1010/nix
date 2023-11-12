---
layout: page
title: osx/base64 (English)
description: "Encode and decode using Base64 representation."
content_hash: 58fd5294d667ce1571771c449b2736d2796ebcaa
last_modified_at: 2023-11-12
related_topics:
  - title: español version
    url: /es/osx/base64.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/osx/base64.html
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

Encode and decode using Base64 representation.
More information: <https://www.unix.com/man-page/osx/1/base64/>.

- Encode a file:

`base64 --input=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">plain_file</span>

- Decode a file:

`base64 --decode --input=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">base64_file</span>

- Encode from `stdin`:

`echo -n "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">plain_text</span>`" | base64`

- Decode from `stdin`:

`echo -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">base64_text</span>` | base64 --decode`

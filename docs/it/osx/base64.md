---
layout: page
title: osx/base64 (italiano)
description: "Codifica e decodifica utilizzando la rappresentazione in base64."
content_hash: 9bd88f3f10ce823c18a954ea26d74d2f9373b7c5
last_modified_at: 2024-10-13
related_topics:
  - title: English version
    url: /en/osx/base64.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/base64.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/osx/base64.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/osx/base64.html
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

Codifica e decodifica utilizzando la rappresentazione in base64.
Maggiori informazioni: <https://keith.github.io/xcode-man-pages/base64.1.html>.

- Codifica un file:

`base64 --input=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_da_codificare</span>

- Decodifica un file:

`base64 --decode --input=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_da_decodificare</span>

- Codifica da `stdin`:

`echo -n "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">testo_da_codificare</span>`" | base64`

- Decodifica da `stdin`:

`echo -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">testo_da_decodificare</span>` | base64 --decode`

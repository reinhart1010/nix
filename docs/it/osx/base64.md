---
layout: page
title: osx/base64 (italiano)
description: "Codifica e decodifica utilizzando la rappresentazione in base64."
content_hash: 4032b989bff00c2335d9d49f734e0719ad8e72b2
last_modified_at: 2023-12-29
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
  - title: português (Brasil) version
    url: /pt_BR/osx/base64.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/base64.html
    icon: bi bi-globe
tldri18n_status: 2
---
# base64

Codifica e decodifica utilizzando la rappresentazione in base64.
Maggiori informazioni: <https://www.unix.com/man-page/osx/1/base64/>.

- Codifica un file:

`base64 --input=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_da_codificare</span>

- Decodifica un file:

`base64 --decode --input=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_da_decodificare</span>

- Codifica da `stdin`:

`echo -n "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">testo_da_codificare</span>`" | base64`

- Decodifica da `stdin`:

`echo -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">testo_da_decodificare</span>` | base64 --decode`

---
layout: page
title: osx/base64 (português (Brasil))
description: "Codifica e decodifica usando a representação Base64."
content_hash: 86b490466bf30d33b1a9f5a4913a01dcfe1bf1d1
last_modified_at: 2024-01-31
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
  - title: italiano version
    url: /it/osx/base64.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/base64.html
    icon: bi bi-globe
tldri18n_status: 2
---
# base64

Codifica e decodifica usando a representação Base64.
Mais informações: <https://keith.github.io/xcode-man-pages/base64.1.html>.

- Codifica um arquivo:

`base64 --input=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo</span>

- Decodifica um arquivo:

`base64 --decode --input=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo_base64</span>

- Codifica de `stdin`:

`echo -n "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">texto</span>`" | base64`

- Decodifica de `stdin`:

`echo -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">texto_base64</span>` | base64 --decode`

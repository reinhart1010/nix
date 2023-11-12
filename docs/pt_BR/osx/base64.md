---
layout: page
title: osx/base64 (português (Brasil))
description: "Codifica e decodifica usando a representação Base64."
content_hash: 77846bcefbe5aed8fc41f895becdb1a74fa4206f
last_modified_at: 2023-11-12
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
Mais informações: <https://www.unix.com/man-page/osx/1/base64/>.

- Codificar um arquivo:

`base64 --input=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo</span>

- Decodificar um arquivo:

`base64 --decode --input=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo_base64</span>

- Codificar de `stdin`:

`echo -n "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">texto</span>`" | base64`

- Decodificar de `stdin`:

`echo -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">texto_base64</span>` | base64 --decode`

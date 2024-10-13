---
layout: page
title: osx/base64 (español)
description: "Codifica y decodifica usando la representación Base64."
content_hash: 8789962333b41ee7c5e7bdc2efb174c97d4ce9d9
last_modified_at: 2024-10-13
related_topics:
  - title: English version
    url: /en/osx/base64.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/osx/base64.html
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

Codifica y decodifica usando la representación Base64.
Más información: <https://keith.github.io/xcode-man-pages/base64.1.html>.

- Codifica un archivo:

`base64 --input=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo_plano</span>

- Decodifica un archivo:

`base64 --decode --input=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">base64_archivo</span>

- Codifica desde `stdin`:

`echo -n "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">texto_plano</span>`" | base64`

- Decodifica desde `stdin`:

`echo -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">base64_texto</span>` | base64 --decode`

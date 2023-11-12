---
layout: page
title: osx/base64 (español)
description: "Codifica y decodifica usando la repesentación Base64."
content_hash: e696d8a99d38b724ee490e1e5cfbaf81d2c2b113
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/osx/base64.html
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

Codifica y decodifica usando la repesentación Base64.
Más información: <https://www.unix.com/man-page/osx/1/base64/>.

- Codifica un archivo:

`base64 --input=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo_plano</span>

- Decodifica un archivo:

`base64 --decode --input=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">base64_archivo</span>

- Codifica desde `stdin`:

`echo -n "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">texto_plano</span>`" | base64`

- Decodifica desde `stdin`:

`echo -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">base64_texto</span>` | base64 --decode`

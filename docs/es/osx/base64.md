---
layout: page
title: osx/base64 (español)
description: "Codifica y decodifica usando la repesentación Base64."
content_hash: 5aa26b05e51f38f84128ad99aa5f2bd70cec1c87
related_topics:
  - title: English version
    url: /en/osx/base64.html
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
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># base64

Codifica y decodifica usando la repesentación Base64.
Más información: <https://www.unix.com/man-page/osx/1/base64/>.

- Codifica un archivo:

`base64 --input=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo_plano</span>

- Decodifica un archivo:

`base64 --decode --input=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">base64_archivo</span>

- Codifica desde stdin:

`echo -n "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">texto_plano</span>`" | base64`

- Decodifica desde stdin:

`echo -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">base64_texto</span>` | base64 --decode`

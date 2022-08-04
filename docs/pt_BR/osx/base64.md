---
layout: page
title: osx/base64 (português (Brasil))
description: "Codifica e decodifica usando a representação Base64."
content_hash: e0d25e547fc9a3d84998caf0734d32199274fec3
related_topics:
  - title: English version
    url: /en/osx/base64.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/osx/base64.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/base64.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># base64

Codifica e decodifica usando a representação Base64.
Mais informações: <https://www.unix.com/man-page/osx/1/base64/>.

- Codificar um arquivo:

`base64 --input=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo</span>

- Decodificar um arquivo:

`base64 --decode --input=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo_base64</span>

- Codificar de stdin:

`echo -n "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">texto</span>`" | base64`

- Decodificar de stdin:

`echo -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">texto_base64</span>` | base64 --decode`

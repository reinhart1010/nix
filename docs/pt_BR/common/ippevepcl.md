---
layout: page
title: common/ippevepcl (português (Brasil))
description: "Imprime em impressoras laser HP PCL a preto e branco."
content_hash: 2502d18ce007e2b7ac81deb76d1f26db932db4ed
last_modified_at: 2023-12-30
related_topics:
  - title: English version
    url: /en/common/ippevepcl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ippevepcl

Imprime em impressoras laser HP PCL a preto e branco.
Suporta arquivos HP PCL, PWG Raster and Apple Raster.
Veja também: `ippevepcl`, `ippeveprinter`.
Mais informações: <https://openprinting.github.io/cups/doc/man-ippevepcl.html>.

- Imprime um arquivo para `stdout` (mensagens de estado e progresso são enviadas para `stderr`):

`ippeveps `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>

- Imprime um arquivo de `stdin` para `stdout`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wget -O - https://examplewebsite.com/file</span>` | ippeveps`

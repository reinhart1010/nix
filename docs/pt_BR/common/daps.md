---
layout: page
title: common/daps (português (Brasil))
description: "DAPS é um programa de código aberto para transformar DocBook XML em formatos de saída como HTML ou PDF."
content_hash: 9170428201b11ea83985ccc139d3b7269e1cf4ab
related_topics:
  - title: English version
    url: /en/common/daps.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># daps

DAPS é um programa de código aberto para transformar DocBook XML em formatos de saída como HTML ou PDF.
Mais informações: <https://opensuse.github.io/daps/doc/index.html>.

- Verifica se um arquivo DocBook XML é válido:

`daps -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.xml</span>` validate`

- Converte um arquivo DocBook XML para PDF:

`daps -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.xml</span>` pdf`

- Converte um arquivo DocBook XML em um único arquivo HTML:

`daps -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.xml</span>` html --single`

- Exibe ajuda:

`daps --help`

- Exibe versão:

`daps --version`

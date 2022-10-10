---
layout: page
title: osx/du (português (Brasil))
description: "Uso do Disco: estima e resume o uso do espaço de arquivos e diretórios."
content_hash: 0c1cb3c2d850c429ce8513c94ee1f251367a3b36
related_topics:
  - title: English version
    url: /en/osx/du.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/osx/du.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/du.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># du

Uso do Disco: estima e resume o uso do espaço de arquivos e diretórios.
Mais informações: <https://ss64.com/osx/du.html>.

- Lista os tamanhos de um diretório e quaisquer subdiretórios, na unidade fornecida (KiB/MiB/GiB):

`du -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">k|m|g</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/diretório</span>

- Lista os tamanhos de um diretório e quaisquer subdiretórios, em formato legível (ou seja, selecionando automaticamente a unidade apropriada para cada tamanho):

`du -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/diretório</span>

- Exibe o tamanho de um único diretório, em unidades legíveis:

`du -sh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/diretório</span>

- Lista os tamanhos legíveis de um diretório e de todos os arquivos e diretórios dentro dele:

`du -ah `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/diretório</span>

- Lista os tamanhos legíveis de um diretório e quaisquer subdiretórios, até N níveis de profundidade:

`du -h -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">N</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/diretório</span>

- Lista o tamanho legível de todos os arquivos `.jpg` nos subdiretórios do diretório atual e exibe um total cumulativo no final:

`du -ch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*/*.jpg</span>

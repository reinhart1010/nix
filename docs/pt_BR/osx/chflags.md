---
layout: page
title: osx/chflags (português (Brasil))
description: "Altera flags de arquivo ou diretório."
content_hash: c423bb9fb0273155b039e269561f3904e4637e18
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/osx/chflags.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/chflags.html
    icon: bi bi-globe
tldri18n_status: 2
---
# chflags

Altera flags de arquivo ou diretório.
Mais informações: <https://ss64.com/osx/chflags.html>.

- Define a flag `hidden` para um arquivo:

`chflags `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hidden</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>

- Remove a flag `hidden` de um arquivo:

`chflags `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nohidden</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>

- Define recursivamente a flag `uchg` para um diretório:

`chflags -R `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uchg</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/diretório</span>

- Remove recursivamente a flag `uchg` de um diretório:

`chflags -R `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nouchg</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/diretório</span>

---
layout: page
title: osx/chflags (português (Brasil))
description: "Altera flags de arquivo ou diretório."
content_hash: d74805aeac266b718ea11525f924b9dd9a73b44c
last_modified_at: 2024-01-31
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
Mais informações: <https://keith.github.io/xcode-man-pages/chflags.1.html>.

- Define a flag `hidden` para um arquivo:

`chflags `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hidden</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>

- Remove a flag `hidden` de um arquivo:

`chflags `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nohidden</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>

- Define recursivamente a flag `uchg` para um diretório:

`chflags -R `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uchg</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/diretório</span>

- Remove recursivamente a flag `uchg` de um diretório:

`chflags -R `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nouchg</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/diretório</span>

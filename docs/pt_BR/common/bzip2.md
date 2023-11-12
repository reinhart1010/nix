---
layout: page
title: common/bzip2 (português (Brasil))
description: "Um compressor de arquivos que utiliza o algoritmo Burrows–Wheeler."
content_hash: 43c080332fdd4ad1a2439b7a765b1faf9b46f747
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/bzip2.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/bzip2.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/bzip2.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># bzip2

Um compressor de arquivos que utiliza o algoritmo Burrows–Wheeler.
Mais informações: <https://manned.org/bzip2>.

- Compactar um arquivo:

`bzip2 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo</span>

- Descompactar um arquivo:

`bzip2 -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo.bz2</span>

- Descompactar um arquivo exibindo o conteúdo no terminal:

`bzip2 -dc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo.bz2</span>

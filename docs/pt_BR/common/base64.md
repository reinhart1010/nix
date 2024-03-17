---
layout: page
title: common/base64 (português (Brasil))
description: "Codifica ou decodifica um arquivo ou uma entrada padrão (`stdin`) de/para Base64, para uma saída padrão (`stdout`)."
content_hash: 0692ac03c5095b2da73ef1a5d75d2bb6b0a92707
last_modified_at: 2024-03-17
related_topics:
  - title: Deutsch version
    url: /de/common/base64.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/base64.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/base64.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/base64.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/base64.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/base64.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/base64.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/base64.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/base64.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/base64.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># base64

Codifica ou decodifica um arquivo ou uma entrada padrão (`stdin`) de/para Base64, para uma saída padrão (`stdout`).
Mais informações: <https://www.gnu.org/software/coreutils/base64>.

- Codifica o conteúdo de um arquivo para base64 e grava o resultado em `stdout`:

`base64 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_arquivo</span>

- Decodifica o conteúdo de um arquivo em base64 e grava o resultado em `stdout`:

`base64 --decode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_arquivo</span>

- Codifica a partir de `stdin`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">algum_comando</span>` | base64`

- Decodifica a partir de `stdin`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">algum_comando</span>` | base64 --decode`

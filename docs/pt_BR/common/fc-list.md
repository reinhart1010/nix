---
layout: page
title: common/fc-list (português (Brasil))
description: "Exibe todas as fontes disponíveis no sistema."
content_hash: bc328ddd06bb7a9bd3863440297ef70caa8b4d06
last_modified_at: 2025-01-05
related_topics:
  - title: English version
    url: /en/common/fc-list.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/fc-list.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/fc-list.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/fc-list.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># fc-list

Exibe todas as fontes disponíveis no sistema.
Mais informações: <https://manned.org/fc-list>.

- Retorna uma lista de fontes instaladas no seu sistema:

`fc-list`

- Retorna uma lista de fontes com um dado nome:

`fc-list | grep '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">DejaVu Serif</span>`'`

- Retorna o número de fontes instaladas no seu sistema:

`fc-list | wc -l`

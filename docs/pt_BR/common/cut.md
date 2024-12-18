---
layout: page
title: common/cut (português (Brasil))
description: "Recorta campos do `stdin` ou de arquivos."
content_hash: 7d3fbe356625c3e3b266a6bbf87697ee27af8ded
last_modified_at: 2024-12-18
related_topics:
  - title: Deutsch version
    url: /de/common/cut.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/cut.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/cut.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/cut.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/cut.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/cut.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/cut.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># cut

Recorta campos do `stdin` ou de arquivos.
Mais informações: <https://www.gnu.org/software/coreutils/manual/html_node/cut-invocation.html>.

- Imprime um intervalo específico de caracteres/campos de cada linha:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>` | cut --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">characters|fields</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1|1,10|1-10|1-|-10</span>

- Imprime um intervalo de campos de cada linha com um delimitador específico:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>` | cut --delimiter "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">,</span>`" --fields `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>

- Imprime um intervalo de caracteres de cada linha de um arquivo específico:

`cut --characters `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>

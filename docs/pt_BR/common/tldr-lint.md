---
layout: page
title: common/tldr-lint (português (Brasil))
description: "Faz lint e formata páginas `tldr`."
content_hash: be27a99dc1e860202c15af256a0450252e9b6a39
last_modified_at: 2024-10-04
related_topics:
  - title: English version
    url: /en/common/tldr-lint.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/tldr-lint.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/tldr-lint.html
    icon: bi bi-globe
  - title: sh version
    url: /sh/common/tldr-lint.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/tldr-lint.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/tldr-lint.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># tldr-lint

Faz lint e formata páginas `tldr`.
Mais informações: <https://github.com/tldr-pages/tldr-lint>.

- Faz lint de todas páginas:

`tldr-lint `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">diretorio_paginas</span>

- Formata uma página específica para `stdout`:

`tldr-lint --format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">page.md</span>

- Formata todas as páginas no mesmo lugar em que estão:

`tldr-lint --format --in-place `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">diretorio_pagina</span>

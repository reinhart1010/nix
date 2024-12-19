---
layout: page
title: common/atrm (español)
description: "Elimina trabajos programados por comandos `at` o `batch`."
content_hash: 79d8ac929335e8cdeec5d1f5ad2fd5b49c0fc75a
last_modified_at: 2024-12-19
related_topics:
  - title: English version
    url: /en/common/atrm.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/atrm.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/atrm.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/atrm.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/atrm.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/atrm.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># atrm

Elimina trabajos programados por comandos `at` o `batch`.
Para encontrar los números de trabajo usa `atq`.
Más información: <https://manned.org/atrm>.

- Elimina el trabajo número 10:

`atrm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>

- Elimina varios trabajos, separados por espacios:

`atrm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">15</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">17</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">22</span>

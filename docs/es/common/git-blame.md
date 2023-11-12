---
layout: page
title: common/git-blame (español)
description: "Muestra el hash del commit y el último autor de cada línea de un archivo."
content_hash: c33bc08ee6f1d9f322a5990402a28fa823a91382
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/git-blame.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-blame.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-blame.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-blame.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/git-blame.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-blame.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-blame.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># git blame

Muestra el hash del commit y el último autor de cada línea de un archivo.
Más información: <https://git-scm.com/docs/git-blame>.

- Muestra el archivo con el nombre del autor y el hash del commit en cada línea:

`git blame `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo</span>

- Muestra el archivo con correo electrónico del autor y hash del commit en cada línea:

`git blame -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo</span>

---
layout: page
title: common/tlmgr-platform (español)
description: "Administra las plataformas TeX Live."
content_hash: 846766bed6f11d681f3039e37d0a9d5f0a99aecf
last_modified_at: 2024-11-17
related_topics:
  - title: English version
    url: /en/common/tlmgr-platform.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/tlmgr-platform.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/tlmgr-platform.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/tlmgr-platform.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/tlmgr-platform.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># tlmgr platform

Administra las plataformas TeX Live.
Más información: <https://www.tug.org/texlive/tlmgr.html>.

- Lista todas las plataformas disponibles en el repositorio de paquetes:

`tlmgr platform list`

- Añade los ejecutables para una plataforma específica:

`sudo tlmgr platform add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">plataforma</span>

- Elimina los ejecutables para una plataforma específica:

`sudo tlmgr platform remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">plataforma</span>

- Auto detecta y cambia a la plataforma actual:

`sudo tlmgr platform set auto`

- Cambia a una plataforma específica:

`sudo tlmgr platform set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">plataforma</span>

---
layout: page
title: common/josm (español)
description: "Editor extensible de OpenStreetMap para Java 8+."
content_hash: 06a2f2bbd32e023ceb90d61f7eb33d6067052d0a
last_modified_at: 2024-12-25
related_topics:
  - title: English version
    url: /en/common/josm.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/josm.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/josm.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># josm

Editor extensible de OpenStreetMap para Java 8+.
Más información: <https://josm.openstreetmap.de/>.

- Abrir JOSM:

`josm`

- Inicia JOSM en modo maximizado:

`josm --maximize`

- Inicia JOSM y establece un idioma específico:

`josm --language `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sp</span>

- Inicia JOSM y restablece todas las preferencias a sus valores predeterminados:

`josm --reset-preferences`

- Inicia JOSM y descarga un área delimitada:

`josm --download `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">minlat,minlon,maxlat,maxlon</span>

- Inicia JOSM y descarga un área delimitada específica como GPS crudo:

`josm --downloadgps `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">minlat,minlon,maxlat,maxlon</span>

- Inicia JOSM sin complementos (plugins):

`josm --skip-plugins`

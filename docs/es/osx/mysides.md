---
layout: page
title: osx/mysides (español)
description: "Añade, lista y elimina favoritos del Finder."
content_hash: 3d57a448eede084e7fd3589d87d2ee40ef9af7d4
last_modified_at: 2023-11-22
related_topics:
  - title: English version
    url: /en/osx/mysides.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/osx/mysides.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># mysides

Añade, lista y elimina favoritos del Finder.
Más información: <https://github.com/mosen/mysides>.

- Lista favoritos de la barra lateral:

`mysides list`

- Añade un nuevo elemento al final de los favoritos de la barra lateral:

`mysides add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ejemplo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file:///Usuarios/Compartidos/ejemplo</span>

- Elimina un elemento por su nombre:

`mysides remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ejemplo</span>

- Añade el directorio actual a la barra lateral:

`mysides add $(basename $(pwd)) file:///$(pwd)`

- Elimina el directorio actual de la barra lateral:

`mysides remove $(basename $(pwd))`

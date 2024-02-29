---
layout: page
title: linux/aur (español)
description: "Construye paquetes desde el AUR y gestiona repositorios locales."
content_hash: 8b58599ecde2ff50039d107c062367066fb95192
last_modified_at: 2024-02-29
related_topics:
  - title: English version
    url: /en/linux/aur.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/aur.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># aur

Construye paquetes desde el AUR y gestiona repositorios locales.
Nota: Es necesario establecer un repositorio local en `/etc/pacman.conf` e instalar `vifm` para que funcione completamente.
Más información: <https://github.com/aurutils/aurutils>.

- Busca un paquete en la base de datos del AUR:

`aur search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">palabra_clave</span>

- Descarga un paquete y sus dependencias desde el AUR, los compila y añade a un repositorio local:

`aur sync `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete</span>

- [l]ista paquetes disponibles en tu repositorio local:

`aur repo --list`

- Act[u]aliza los paquetes del repositorio local:

`aur sync --upgrades`

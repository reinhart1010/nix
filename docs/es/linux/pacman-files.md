---
layout: page
title: linux/pacman-files (español)
description: "Utilidad de manejo de paquetes de Arch Linux."
content_hash: 9dbe7c4752a07e4fdf1f344354b91b0b7a025da5
last_modified_at: 2024-12-28
related_topics:
  - title: Deutsch version
    url: /de/linux/pacman-files.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/pacman-files.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/pacman-files.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/pacman-files.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/pacman-files.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/pacman-files.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/pacman-files.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/pacman-files.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pacman --files

Utilidad de manejo de paquetes de Arch Linux.
Vea también: `pacman`, `pkgfile`.
Más información: <https://manned.org/pacman.8>.

- Actualiza la base de datos de paquetes:

`sudo pacman -Fy`

- Encuentra el paquete que posee un archivo específico:

`pacman -F `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo</span>

- Encuentra el paquete que posee un archivo específico, utilizando una e[x]presión regular:

`pacman -Fx '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">expresión_regular</span>`'`

- Lista solo los nombres de los paquetes:

`pacman -Fq `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo</span>

- [L]ista los archivos que hacen parte de un paquete específico:

`pacman -Fl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete</span>

- Muestra la ayuda:

`pacman -Fh`

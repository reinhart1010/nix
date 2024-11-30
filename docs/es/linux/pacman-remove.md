---
layout: page
title: linux/pacman-remove (español)
description: "Utilidad del administrador de paquetes de Arch Linux."
content_hash: f3fc07720d82bad14b3005dbe071cd7df66f5335
last_modified_at: 2024-11-30
related_topics:
  - title: Deutsch version
    url: /de/linux/pacman-remove.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/pacman-remove.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/pacman-remove.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/pacman-remove.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/pacman-remove.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/pacman-remove.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/pacman-remove.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/pacman-remove.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/pacman-remove.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/pacman-remove.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pacman --remove

Utilidad del administrador de paquetes de Arch Linux.
Vea también: `pacman`.
Más información: <https://manned.org/pacman.8>.

- [R]emueve un paquete y sus dependencias recur[s]ivamente:

`sudo pacman -Rs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete</span>

- [R]emueve un paquete y sus dependencias. [n]o guarda copias de seguridad de los archivos de configuración:

`sudo pacman -Rsn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete</span>

- [R]emueve un paquete sin pedir confirmación:

`sudo pacman -R --noconfirm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete</span>

- [R]emueve los paquetes huérfanos (instalados como [d]ependencias pero no requeridos por algún paquete):

`sudo pacman -Rsn $(pacman -Qdtq)`

- [R]emueve un paquete y ha[c]e lo mismo a todos los paquetes que dependen de él:

`sudo pacman -Rc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete</span>

- Lista e im[p]rime los paquetes que serían afectados (no [R]emueve paquete alguno):

`pacman -Rp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete</span>

- Muestra la ayuda:

`pacman -Rh`

---
layout: page
title: linux/pacman-sync (español)
description: "Utilidad del administrador de paquetes de Arch Linux."
content_hash: df3b1ae765f1fb73e2d74b8185dcc9a775104bd2
last_modified_at: 2024-11-30
related_topics:
  - title: Deutsch version
    url: /de/linux/pacman-sync.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/pacman-sync.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/pacman-sync.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/pacman-sync.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/pacman-sync.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/pacman-sync.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/pacman-sync.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/pacman-sync.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/pacman-sync.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/pacman-sync.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pacman --sync

Utilidad del administrador de paquetes de Arch Linux.
Vea también: `pacman`.
Más información: <https://manned.org/pacman.8>.

- Instala un paquete nuevo:

`sudo pacman -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete</span>

- [S]incroniza y actualiza ([y]) la base de datos de paquetes junto con un sys[u]pgrade (añade `--downloadonly` para solamente descargar los paquetes y no actualizarlos):

`sudo pacman -Syu`

- Actualiza (update) y moderniza ([u]pgrade) todos los paquetes e instala uno nuevo sin solicitar confirmación:

`sudo pacman -Syu --noconfirm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete</span>

- Busca ([s]) la base de datos de paquetes con una expresión regular o palabra clave:

`pacman -Ss "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">patrón_de_búsqueda</span>`"`

- Muestra [i]nformación sobre un paquete:

`pacman -Si `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete</span>

- Sobrescribe archivos conflictivos durante una actualización del paquete:

`sudo pacman -Syu --overwrite `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- [S]incroniza y act[u]aliza todos los paquetes, e ignora un paquete específico (puede ser utilizado más de una vez):

`sudo pacman -Syu --ignore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete1 paquete2 ...</span>

- Elimina paquetes no instalados y repositorios no utilizados de la caché (utiliza las banderas `Sc` para limpiar ([c]) todos los paquetes):

`sudo pacman -Sc`

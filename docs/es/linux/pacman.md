---
layout: page
title: linux/pacman (español)
description: "Arch Linux paquete manager utility."
content_hash: 9547a9365a5701066af89342fa8c97ada5ed69d7
last_modified_at: 2024-10-16
related_topics:
  - title: Deutsch version
    url: /de/linux/pacman.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/pacman.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/linux/pacman.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/pacman.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/pacman.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/pacman.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/pacman.html
    icon: bi bi-globe
  - title: മലയാളം version
    url: /ml/linux/pacman.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/pacman.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/pacman.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/linux/pacman.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/pacman.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/pacman.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/pacman.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/pacman.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pacman

Arch Linux paquete manager utility.
Utilidad del administrador de paquetes de Arch Linux.
Vea también: `pacman-sync`, `pacman-remove`, `pacman-query`, `pacman-upgrade`, `pacman-files`, `pacman-database`, `pacman-deptest`, `pacman-key`, `pacman-mirrors`.
Para comandos equivalentes en otros administradores de paquetes, vea <https://wiki.archlinux.org/title/Pacman/Rosetta>.
Más información: <https://manned.org/pacman.8>.

- Sincroniza y actualiza todos los paquetes:

`sudo pacman -Syu`

- Instala un nuevo paquete:

`sudo pacman -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete</span>

- Elimina un paquete y sus dependencias:

`sudo pacman -Rs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete</span>

- Busca en la base de datos paquetes que contengan un archivo específico:

`pacman -F "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_archivo</span>`"`

- Lista los paquetes y versiones instalados:

`pacman -Q`

- Lista solo los paquetes y versiones instalados explícitamente:

`pacman -Qe`

- Lista los paquetes huérfanos (instalados como dependencias pero que en realidad no son necesarios para ningún paquete):

`pacman -Qtdq`

- Vacía toda la caché de `pacman`:

`sudo pacman -Scc`

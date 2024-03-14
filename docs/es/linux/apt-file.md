---
layout: page
title: linux/apt-file (español)
description: "Busca archivos en paquetes APT, incluyendo los que aún no fueron instalados."
content_hash: c299f38d58b6b2c8641db0dd4a1517aabe075041
last_modified_at: 2024-03-14
related_topics:
  - title: català version
    url: /ca/linux/apt-file.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/apt-file.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/apt-file.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/apt-file.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/apt-file.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/apt-file.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/apt-file.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/apt-file.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/apt-file.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># apt-file

Busca archivos en paquetes APT, incluyendo los que aún no fueron instalados.
Más información: <https://manpages.debian.org/latest/apt-file/apt-file.1.html>.

- Actualiza los metadatos de la base de datos:

`sudo apt update`

- Busca paquetes que contengan el archivo o ruta especificada:

`apt-file search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Muestra el contenido del paquete especificado:

`apt-file list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_paquete</span>

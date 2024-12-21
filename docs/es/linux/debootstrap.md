---
layout: page
title: linux/debootstrap (español)
description: "Crea un sistema básico de Debian."
content_hash: 888d1b8e26db41ff2494b4d00aa60ad5270b61f3
last_modified_at: 2024-12-21
related_topics:
  - title: English version
    url: /en/linux/debootstrap.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/debootstrap.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/debootstrap.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/debootstrap.html
    icon: bi bi-globe
tldri18n_status: 2
---
# debootstrap

Crea un sistema básico de Debian.
Más información: <https://wiki.debian.org/Debootstrap>.

- Crea un sistema de la versión estable de Debian dentro del directorio `debian-root`:

`sudo debootstrap stable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/debian-root/</span>` http://deb.debian.org/debian`

- Crea un sistema mínimo que incluye solo los paquetes necesarios:

`sudo debootstrap --variant=minbase stable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/debian-root/</span>

- Crea un sistema Ubuntu 20.04 dentro del directorio `focal-root` con un espejo local:

`sudo debootstrap focal `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/focal-root/</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file:///ruta/a/mirror/</span>

- Cambia a un sistema de arranque:

`sudo chroot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/root</span>

- Lista las versiones mayores disponibles:

`ls /usr/share/debootstrap/scripts/`

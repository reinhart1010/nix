---
layout: page
title: linux/debtap (español)
description: "Convierte paquetes Debian en paquetes de Arch Linux."
content_hash: 7bef7826f32452fdb8d2f925d5cc5be16f83b562
last_modified_at: 2024-12-21
related_topics:
  - title: English version
    url: /en/linux/debtap.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/debtap.html
    icon: bi bi-globe
tldri18n_status: 2
---
# debtap

Convierte paquetes Debian en paquetes de Arch Linux.
Vea también: `pacman-upgrade`.
Más información: <https://github.com/helixarch/debtap>.

- Actualiza la base de datos de debtap (antes de la primera ejecución):

`sudo debtap --update`

- Convierte el paquete especificado:

`debtap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/paquete.deb</span>

- Convierte el paquete especificado obviando todas las preguntas, excepto para editar archivos de metadatos:

`debtap --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/paquete.deb</span>

- Genera un archivo PKGBUILD:

`debtap --pkgbuild `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/paquete.deb</span>

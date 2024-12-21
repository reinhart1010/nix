---
layout: page
title: linux/dpkg-deb (español)
description: "Empaqueta, desempaqueta y proporciona información sobre archivos Debian."
content_hash: eb6182dfa46625f9da6fa6a19cd16e935de0df20
last_modified_at: 2024-12-21
related_topics:
  - title: English version
    url: /en/linux/dpkg-deb.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/dpkg-deb.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/dpkg-deb.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dpkg-deb

Empaqueta, desempaqueta y proporciona información sobre archivos Debian.
Más información: <https://manned.org/dpkg-deb>.

- Muestra información sobre un paquete:

`dpkg-deb --info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.deb</span>

- Muestra el nombre y la versión del paquete en una línea:

`dpkg-deb --show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.deb</span>

- Lista el contenido del paquete:

`dpkg-deb --contents `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.deb</span>

- Extrae el contenido del paquete en un directorio:

`dpkg-deb --extract `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.deb</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio</span>

- Crea un paquete desde un directorio especificado:

`dpkg-deb --build `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio</span>

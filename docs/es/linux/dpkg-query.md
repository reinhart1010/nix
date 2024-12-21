---
layout: page
title: linux/dpkg-query (español)
description: "Muestra información sobre paquetes instalados."
content_hash: ad1f05ce512b54b9994bd0c92ab43182f0f411aa
last_modified_at: 2024-12-21
related_topics:
  - title: English version
    url: /en/linux/dpkg-query.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/dpkg-query.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/dpkg-query.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/dpkg-query.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dpkg-query

Muestra información sobre paquetes instalados.
Más información: <https://manned.org/dpkg-query.1>.

- Lista todos los paquetes instalados:

`dpkg-query --list`

- Lista de paquetes instalados que coinciden con un patrón:

`dpkg-query --list '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">libc6*</span>`'`

- Lista todos los archivos instalados por un paquete:

`dpkg-query --listfiles `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">libc6</span>

- Muestra información sobre un paquete:

`dpkg-query --status `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">libc6</span>

- Busca paquetes que tengan archivos que coincidan con un patrón:

`dpkg-query --search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/etc/ld.so.conf.d</span>

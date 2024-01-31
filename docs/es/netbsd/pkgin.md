---
layout: page
title: netbsd/pkgin (español)
description: "Gestiona paquetes binarios `pkgsrc` en NetBSD."
content_hash: 512ca4ea5ae88e4ab8147293e01347e80c402f10
last_modified_at: 2024-01-31
related_topics:
  - title: English version
    url: /en/netbsd/pkgin.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/netbsd/pkgin.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/netbsd/pkgin.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pkgin

Gestiona paquetes binarios `pkgsrc` en NetBSD.
Más información: <https://pkgin.net/#usage>.

- Instala un paquete:

`pkgin install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete</span>

- Elimina un paquete y sus dependencias:

`pkgin remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete</span>

- Actualiza todos los paquetes:

`pkgin full-upgrade`

- Busca un paquete:

`pkgin search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">palabra_clave</span>

- Lista los paquetes instalados:

`pkgin list`

- Elimina dependencias innecesarias:

`pkgin autoremove`

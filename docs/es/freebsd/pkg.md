---
layout: page
title: freebsd/pkg (español)
description: "Gestor de paquetes de FreeBSD."
content_hash: 3a785498e6b2804191fcf1720a9222efee56721d
last_modified_at: 2024-02-07
related_topics:
  - title: English version
    url: /en/freebsd/pkg.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/freebsd/pkg.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/freebsd/pkg.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/freebsd/pkg.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pkg

Gestor de paquetes de FreeBSD.
Más información: <https://man.freebsd.org/cgi/man.cgi?query=pkg&sektion=8>.

- Instala un nuevo paquete:

`pkg install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete</span>

- Elimina un paquete:

`pkg delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete</span>

- Actualiza todos los paquetes:

`pkg upgrade`

- Busca un paquete:

`pkg search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">palabra_clave</span>

- Lista los paquetes instalados:

`pkg info`

- Elimina dependencias innecesarias:

`pkg autoremove`

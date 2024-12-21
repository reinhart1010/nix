---
layout: page
title: linux/debchange (español)
description: "Mantiene el archivo debian/log de cambios (changelog) de un paquete fuente de Debian."
content_hash: 16f4fff18cf2c7886e4927292d8fbf445421c435
last_modified_at: 2024-12-21
related_topics:
  - title: English version
    url: /en/linux/debchange.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/debchange.html
    icon: bi bi-globe
tldri18n_status: 2
---
# debchange

Mantiene el archivo debian/log de cambios (changelog) de un paquete fuente de Debian.
Más información: <https://manned.org/debchange.1>.

- Agrega una nueva versión para una subida que no es del mantenedor al registro (log) de cambios:

`debchange --nmu`

- Agrega una entrada de cambio a la versión actual:

`debchange --append`

- Agrega una entrada de cambio para cerrar el fallo con un ID específico:

`debchange --closes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_del_fallo</span>

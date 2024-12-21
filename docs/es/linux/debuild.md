---
layout: page
title: linux/debuild (español)
description: "Construye un paquete Debian desde las fuentes."
content_hash: c371e3acf14c06b12fb7cc87f3e785dd7df48626
last_modified_at: 2024-12-21
related_topics:
  - title: English version
    url: /en/linux/debuild.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/debuild.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/debuild.html
    icon: bi bi-globe
tldri18n_status: 2
---
# debuild

Construye un paquete Debian desde las fuentes.
Más información: <https://manned.org/debuild.1>.

- Construye el paquete en el directorio actual:

`debuild`

- Construye un paquete binario solamente:

`debuild -b`

- No ejecuta lintian después de construir el paquete:

`debuild --no-lintian`

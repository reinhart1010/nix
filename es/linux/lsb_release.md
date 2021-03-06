---
layout: page
title: linux/lsb_release (español)
description: "Proporciona información específica de la distribución y LSB (Linux Standard Base)."
content_hash: 2a09d9a24780cf838ea0c304487684beecc2edb0
related_topics:
  - title: English version
    url: /en/linux/lsb_release.html
    icon: bi bi-globe
---
# lsb_release

Proporciona información específica de la distribución y LSB (Linux Standard Base).
Más información: <https://manned.org/lsb_release>.

- Muestra toda la información disponible:

`lsb_release -a`

- Muestra una descripción del sistema operativo (normalmente el nombre completo):

`lsb_release -d`

- Muestra solo el nombre del sistema operativo (ID) sin el campo nombre:

`lsb_release -i -s`

- Muestra el número de versión y el nombre en clave de la distribución sin el campo de nombre:

`lsb_release -rcs`

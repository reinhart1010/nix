---
layout: page
title: linux/deborphan (español)
description: "Muestra paquetes huérfanos en sistemas operativos usando el administrador de paquetes APT."
content_hash: 71f57e8b17d9725174bd00b543a73f7620b56d3d
last_modified_at: 2024-12-21
related_topics:
  - title: English version
    url: /en/linux/deborphan.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/deborphan.html
    icon: bi bi-globe
tldri18n_status: 2
---
# deborphan

Muestra paquetes huérfanos en sistemas operativos usando el administrador de paquetes APT.
Más información: <https://manned.org/deborphan>.

- Muestra paquetes de biblioteca (de la sección "libs" del repositorio de paquetes) que no son requeridos por otro paquete:

`deborphan`

- Lista paquetes huérfanos de la sección "libs", así como paquetes huérfanos que tienen un nombre que parece un nombre de biblioteca:

`deborphan --guess-all`

- Busca paquetes que son recomendados o sugeridos (pero no requeridos) por otro paquete:

`deborphan --nice-mode`

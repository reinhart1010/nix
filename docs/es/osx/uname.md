---
layout: page
title: osx/uname (español)
description: "Imprime detalles sobre la máquina actual y el sistema operativo que se ejecuta en ella."
content_hash: 0c3d0b354a8e6e35bdf5c39a1d2a0e9ca5ee608b
last_modified_at: 2023-07-10
related_topics:
  - title: English version
    url: /en/osx/uname.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/osx/uname.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/uname.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># uname

Imprime detalles sobre la máquina actual y el sistema operativo que se ejecuta en ella.
Nota: para obtener información adicional sobre el sistema operativo, pruebe el comando `sw_vers`.
Más información: <https://ss64.com/osx/uname.html>.

- Imprime el nombre del kernel:

`uname`

- Muestra la arquitectura del sistema y la información del procesador:

`uname -mp`

- Muestra el nombre, la versión y la versión del kernel:

`uname -srv`

- Muestra el nombre de host del sistema:

`uname -n`

- Muestra toda la información disponible del sistema:

`uname -a`

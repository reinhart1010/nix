---
layout: page
title: osx/uname (español)
description: "Imprime detalles sobre la máquina actual y el sistema operativo que se ejecuta en ella."
content_hash: 5e03d2ee4fbbe912529bb43d925453b473a475b6
last_modified_at: 2024-01-31
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
tldri18n_status: 2
---
# uname

Imprime detalles sobre la máquina actual y el sistema operativo que se ejecuta en ella.
Nota: para obtener información adicional sobre el sistema operativo, pruebe el comando `sw_vers`.
Más información: <https://keith.github.io/xcode-man-pages/uname.1.html>.

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

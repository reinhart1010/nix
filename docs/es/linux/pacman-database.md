---
layout: page
title: linux/pacman-database (español)
description: "Opera en la base de datos de paquetes de Arch Linux."
content_hash: 77b3c9468fbf943c3f1105901e00606dd5569f1a
last_modified_at: 2024-10-15
related_topics:
  - title: Deutsch version
    url: /de/linux/pacman-database.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/pacman-database.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/pacman-database.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/pacman-database.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/pacman-database.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/pacman-database.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/pacman-database.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pacman --database

Opera en la base de datos de paquetes de Arch Linux.
Modifica ciertos atributos de los paquetes instalados.
Vea también: `pacman`.
Más información: <https://manned.org/pacman.8>.

- Marca un paquete como instalado implícitamente:

`sudo pacman --database --asdeps `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete</span>

- Marca un paquete como instalado explícitamente:

`sudo pacman --database --asexplicit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete</span>

- Verifica que todas las dependencias del paquete estén instaladas:

`pacman --database --check`

- Verifica los repositorios para asegurarse de que todas las dependencias especificadas estén disponibles:

`pacman --database --check --check`

- Muestra solo mensajes de error:

`pacman --database --check --quiet`

- Muestra ayuda:

`pacman --database --help`

---
layout: page
title: common/vcpkg (español)
description: "Gestor de paquetes para librerías C/C++."
content_hash: cb3bc10ef3f2ac34940bef72415756460ab1eaea
last_modified_at: 2024-05-06
related_topics:
  - title: English version
    url: /en/common/vcpkg.html
    icon: bi bi-globe
tldri18n_status: 2
---
# vcpkg

Gestor de paquetes para librerías C/C++.
Nota: los paquetes no se instalan en el sistema. Para usarlos, necesitas decirle a tu sistema de compilación (por ejemplo CMake) que use `vcpkg`.
Más información: <https://learn.microsoft.com/en-us/vcpkg/>.

- Construye y añade el paquete `libcurl` al entorno de `vcpkg`:

`vcpkg install curl`

- Construye y añade `zlib` usando la cadena de herramientas `emscripten`:

`vcpkg install --triplet=wasm32-emscripten zlib`

- Busca un paquete:

`vcpkg search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_paquete</span>

- Configura un proyecto CMake para utilizar los paquetes de `vcpkg`:

`cmake -B build -DCMAKE_TOOLCHAIN_FILE=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio_de_instalación_vcpkg</span>`/scripts/buildsystems/vcpkg.cmake`

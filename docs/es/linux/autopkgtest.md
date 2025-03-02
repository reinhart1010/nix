---
layout: page
title: linux/autopkgtest (español)
description: "Ejecuta pruebas sobre paquetes de Debian."
content_hash: 9afb137ce9a12449e2a8eb18eda56c0435f3f597
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/linux/autopkgtest.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/autopkgtest.html
    icon: bi bi-globe
tldri18n_status: 2
---
# autopkgtest

Ejecuta pruebas sobre paquetes de Debian.
Más información: <https://wiki.debian.org/ContinuousIntegration/autopkgtest>.

- Construye el paquete en el directorio actual y ejecuta todas las pruebas directamente en el sistema:

`autopkgtest -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">null</span>

- Ejecuta una prueba específica para el paquete en el directorio actual:

`autopkgtest --test-name=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_prueba</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">null</span>

- Descarga y construye un paquete específico con `apt-get`, luego ejecuta todas las pruebas:

`autopkgtest `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">null</span>

- Prueba el paquete en el directorio actual utilizando un nuevo directorio raíz:

`autopkgtest -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chroot</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/nuevo/directorio</span>

- Prueba el paquete en el directorio actual sin reconstruirlo:

`autopkgtest --no-built-binaries -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">null</span>

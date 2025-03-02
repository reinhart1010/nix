---
layout: page
title: common/pio-debug (español)
description: "Depura proyectos PlatformIO."
content_hash: efd9cd4e17dcb500a8a3be0c55ee54e32dfccb80
last_modified_at: 2024-11-25
related_topics:
  - title: English version
    url: /en/common/pio-debug.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/pio-debug.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/pio-debug.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pio debug

Depura proyectos PlatformIO.
Más información: <https://docs.platformio.org/en/latest/core/userguide/cmd_debug.html>.

- Depura el proyecto PlatformIO del directorio actual:

`pio debug`

- Depura un proyecto PlatformIO específico:

`pio debug --project-dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/proyecto_platformio</span>

- Depura un ambiente específico:

`pio debug --environment `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ambiente</span>

- Depura un proyecto PlatformIO utilizando un archivo de configuración específico:

`pio debug --project-conf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/platformio.ini</span>

- Depura un proyecto PlatformIO usando el depurador `gdb`:

`pio debug --interface=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gdb</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">opciones_de_gdb</span>

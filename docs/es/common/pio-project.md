---
layout: page
title: common/pio-project (español)
description: "Administra proyectos PlatformIO."
content_hash: a69125104923b8183f8b7ed1b881b174a53ae514
last_modified_at: 2024-12-03
related_topics:
  - title: English version
    url: /en/common/pio-project.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/pio-project.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/pio-project.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pio project

Administra proyectos PlatformIO.
Más información: <https://docs.platformio.org/en/latest/core/userguide/project/>.

- Inicializa un nuevo proyecto PlatformIO:

`pio project init`

- Inicializa un nuevo proyecto PlatformIO en un directorio específico:

`pio project init --project-dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio_del_proyecto</span>

- Inicializa un nuevo proyecto PlatformIO, especificando un ID del board:

`pio project init --board `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ATmega328P|uno|...</span>

- Inicializa un nuevo proyecto PlatformIO, especificando una o más opciones para el proyecto:

`pio project init --project-option="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">opción</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">valor</span>`" --project-option="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">opción</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">valor</span>`"`

- Muestra la configuración de un proyecto:

`pio project config`

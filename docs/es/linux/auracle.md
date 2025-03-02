---
layout: page
title: linux/auracle (español)
description: "Herramienta de línea de comandos utilizada para interactuar con el repositorio de usuarios de Arch Linux, comúnmente conocido como AUR."
content_hash: 56023a1440d85d295b24ab35d9997baeb9fdca3d
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/linux/auracle.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/auracle.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/auracle.html
    icon: bi bi-globe
tldri18n_status: 2
---
# auracle

Herramienta de línea de comandos utilizada para interactuar con el repositorio de usuarios de Arch Linux, comúnmente conocido como AUR.
Más información: <https://github.com/falconindy/auracle>.

- Muestra los paquetes del AUR que coinciden con una expresión regular:

`auracle search '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">expresión_regular</span>`'`

- Muestra información sobre uno o más paquetes del AUR:

`auracle info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete1 paquete2 ...</span>

- Muestra el archivo `PKGBUILD` (información de construcción) de uno o más paquetes del AUR:

`auracle show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete1 paquete2 ...</span>

- Muestra actualizaciones para los paquetes del AUR instalados:

`auracle outdated`

---
layout: page
title: osx/port (español)
description: "Gestor de paquetes para macOS."
content_hash: 41a3b53a28612a6bad6502714d301db72d3fc6c8
related_topics:
  - title: English version
    url: /en/osx/port.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/port.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># port

Gestor de paquetes para macOS.
Más información: <https://www.macports.org>.

- Busca un paquete:

`port search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">termino_de_busqueda</span>

- Instala un paquete:

`sudo port install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_paquete</span>

- Lista los paquetes instalados:

`port installed`

- Actualiza port y trae la última lista de paquetes disponibles:

`sudo port selfupdate`

- Actualiza los paquetes desactualizados:

`sudo port upgrade outdated`

- Remueve versiones antiguas de paquetes instalados:

`sudo port uninstall inactive`

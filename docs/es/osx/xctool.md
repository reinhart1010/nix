---
layout: page
title: osx/xctool (español)
description: "Herramienta para construir proyectos Xcode."
content_hash: bbe7dbd4c1e1c9da821690c04e22dcd806e6dbca
last_modified_at: 2023-10-22
related_topics:
  - title: English version
    url: /en/osx/xctool.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/xctool.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># xctool

Herramienta para construir proyectos Xcode.
Más información: <https://github.com/facebookarchive/xctool>.

- Construye un proyecto sin ningún espacio de trabajo:

`xctool -project `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">TuProyecto.xcodeproj</span>` -scheme `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">SuEsquema</span>` build`

- Construye un proyecto que forma parte de un espacio de trabajo:

`xctool -workspace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">TuEspacioDeTrabajo.xcworkspace</span>` -scheme `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">TuEsquema</span>` build`

- Limpia, construye y ejecuta todas las pruebas:

`xctool -workspace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">TuEspacioTrabajo.xcworkspace</span>` -scheme `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">TuEsquema</span>` clean build test`

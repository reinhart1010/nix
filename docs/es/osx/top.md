---
layout: page
title: osx/top (español)
description: "Muestra información dinámica en tiempo real sobre los procesos en ejecución."
content_hash: 6b3438856b4f6f4c5e785c41ccec9720bb66113e
last_modified_at: 2024-11-16
related_topics:
  - title: English version
    url: /en/osx/top.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/osx/top.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/top.html
    icon: bi bi-globe
tldri18n_status: 2
---
# top

Muestra información dinámica en tiempo real sobre los procesos en ejecución.
Más información: <https://keith.github.io/xcode-man-pages/top.1.html>.

- Inicia top, todas las opciones están disponibles en la interfaz:

`top`

- Inicia top ordenando los procesos por tamaño de memoria interna (orden por defecto - ID del proceso):

`top -o mem`

- Inicia top ordenando los procesos primero por CPU, luego por tiempo de ejecución:

`top -o cpu -O time`

- Inicia top mostrando sólo los procesos que pertenecen a un usuario determinado:

`top -user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usuario</span>

- Muestra información de ayuda sobre comandos interactivos:

`?`

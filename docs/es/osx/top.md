---
layout: page
title: osx/top (español)
description: "Muestra información dinámica en tiempo real sobre los procesos en ejecución."
content_hash: 8eb82657085ff8a8414cdd64f2a4ef8daec577f6
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/osx/top.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/top.html
    icon: bi bi-globe
tldri18n_status: 2
---
# top

Muestra información dinámica en tiempo real sobre los procesos en ejecución.
Más información: <https://ss64.com/osx/top.html>.

- Inicia top, todas las opciones están disponibles en la interfaz:

`top`

- Inicia top ordenando los procesos por tamaño de memoria interna (orden por defecto - ID del proceso):

`top -o mem`

- Inicia top ordenando los procesos primero por CPU, luego por tiempo de ejecución:

`top -o cpu -O time`

- Inicia top mostrando sólo los procesos que pertenecen a un usuario determinado:

`top -user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_usuario</span>

- Obtener ayuda sobre comandos interactivos:

`?`

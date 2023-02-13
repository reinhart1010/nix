---
layout: page
title: common/amass-db (español)
description: "interactúa con una base de datos Amass."
content_hash: a5dcadbc18b688b9fdca7f1f23758aa38ae53b6f
last_modified_at: 2023-02-13
related_topics:
  - title: English version
    url: /en/common/amass-db.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/amass-db.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># amass db

interactúa con una base de datos Amass.
Más información: <https://github.com/OWASP/Amass/blob/master/doc/user_guide.md#the-db-subcommand>.

- Lista de todas las enumeraciones realizadas en la base de datos:

`amass db -dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio_base_de_datos</span>` -list`

- Muestra resultados para un índice de enumeración y un nombre de dominio especificados:

`amass db -dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio_base_de_datos</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_dominio</span>` -enum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">indice_de_lista</span>` -show`

- Lista todos los subdominios encontrados en un dominio dentro de una enumeración:

`amass db -dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio_base_de_datos</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_dominio</span>` -enum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">indice_de_lista</span>` -names`

- Muestra un resumen de los subdominios encontrados dentro de una enumeración:

`amass db -dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio_base_de_datos</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_dominio</span>` -enum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">indice_de_lista</span>` -summary`

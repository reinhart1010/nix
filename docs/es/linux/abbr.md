---
layout: page
title: linux/abbr (español)
description: "Administra abreviaturas del intérprete de comandos fish."
content_hash: 22fd78105ffb3d973f7065ae303106d4ba218ac8
last_modified_at: 2024-06-11
related_topics:
  - title: català version
    url: /ca/linux/abbr.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/abbr.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/abbr.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/linux/abbr.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/abbr.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/abbr.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/abbr.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/abbr.html
    icon: bi bi-globe
tldri18n_status: 2
---
# abbr

Administra abreviaturas del intérprete de comandos fish.
Las palabras definidas por el usuario se reemplazan con frases más largas después de ingresarlas.
Más información: <https://fishshell.com/docs/current/cmds/abbr.html>.

- Añade una nueva abreviatura:

`abbr --add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_abreviatura</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">argumentos_del_comando</span>

- Cambia el nombre de una abreviatura existente:

`abbr --rename `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_antiguo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_nuevo</span>

- Borra una abreviatura existente:

`abbr --erase `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_abreviatura</span>

- Importa las abreviaturas definidas en otro host a través de SSH:

`ssh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_host</span>` abbr --show | source`

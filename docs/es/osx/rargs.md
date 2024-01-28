---
layout: page
title: osx/rargs (español)
description: "Ejecuta un comando por cada línea de entrada estándar."
content_hash: 893f6978d701aca76e18125f9fe485919d8bbde3
last_modified_at: 2024-01-28
related_topics:
  - title: English version
    url: /en/osx/rargs.html
    icon: bi bi-globe
tldri18n_status: 2
---
# rargs

Ejecuta un comando por cada línea de entrada estándar.
Similar a `xargs`, pero con soporte de coincidencia de patrones.
Más información: <https://github.com/lotabout/rargs>.

- Ejecuta un comando por cada línea de entrada, como `xargs` (`{0}` indica donde sustituir en el texto):

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>` | rargs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>` {0}`

- Imprime los comandos que se ejecutarían en vez de ejecutarlos:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>` | rargs -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>` {0}`

- Elimina la extensión `.bak` de todos los archivos de una lista:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>` | rargs -p '(.*).bak mv {0} {1}`

- Ejecuta comandos en paralelo:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>` | rargs -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">máxima_cantidad_de_procesos</span>

- Lee líneas de entrada separadas por el caracter `NUL` (`\0`) en vez de `LF` (`\n`):

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>` | rargs -0 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>` {0}`

---
layout: page
title: linux/export (español)
description: "Exporta variables de un intérprete de comandos (shell) a procesos hijos."
content_hash: eaea0b573bc6b3442689ff3248bb0fbd198d5a5b
last_modified_at: 2024-12-20
related_topics:
  - title: English version
    url: /en/linux/export.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/export.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/export.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/export.html
    icon: bi bi-globe
tldri18n_status: 2
---
# export

Exporta variables de un intérprete de comandos (shell) a procesos hijos.
Más información: <https://www.gnu.org/software/bash/manual/bash.html#index-export>.

- Establece una variable de entorno:

`export `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">VARIABLE</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">valor</span>

- Quita una variable de entorno:

`export -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">VARIABLE</span>

- Exporta una función a los procesos hijos:

`export -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">NOMBRE_FUNCION</span>

- Añade una ruta a la variable de ambiente `PATH`:

`export PATH=$PATH:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/añadir</span>

- Muestra una lista de variables exportadas activas en forma de comando de interfaz de comandos (shell command form):

`export -p`

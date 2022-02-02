---
layout: page
title: common/tree (español)
description: "Muestra los contenidos del directorio actual en forma de árbol."
content_hash: e3a953f7b285bc6d78b6dbce0ac4f6f53db0f066
related_topics:
  - title: English version
    url: /en/common/tree.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/tree.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/tree.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/tree.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/tree.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># tree

Muestra los contenidos del directorio actual en forma de árbol.
Más información: <http://mama.indstate.edu/users/ice/tree/>.

- Imprime archivos y directories hasta `num` niveles de profundidad (donde 1 significa el directorio actual):

`tree -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">num</span>

- Imprime solo directorios:

`tree -d`

- Imprime también archivos ocultos, coloreando la salida:

`tree -a -C`

- Imprime el árbol sin sangría, mostrando la ruta completa en su lugar (use `-N` para evitar escapar caracteres no imprimibles):

`tree -i -f`

- Imprime el tamaño de cada archivo y el tamaño total de cada directorio en formato legible para humanos:

`tree -s -h --du`

- Imprime archivos dentro de la jerarquía de árbol, especificando un patrón comodín, excluyendo los directorios que no contengan archivos coincidentes:

`tree -P '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.txt</span>`' --prune`

- Imprime archivos dentro de la jerarquía de árbol, especificando un patrón, excluyendo los directorios que no sean ancestros del especificado:

`tree -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_directorio</span>` --matchdirs --prune`

- Imprime el árbol ignorando los directorios especificados:

`tree -I '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_directorio1|nombre_del_directorio2</span>`'`

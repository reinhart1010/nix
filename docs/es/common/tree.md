---
layout: page
title: common/tree (español)
description: "Muestra los contenidos del directorio actual en forma de árbol."
content_hash: a45da82e6fa1c033e8d7bfc6a42e8c99580fe1bc
last_modified_at: 2024-05-23
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
tldri18n_status: 2
---
# tree

Muestra los contenidos del directorio actual en forma de árbol.
Más información: <https://manned.org/man/tree>.

- Imprime archivos y directorios hasta `num` niveles de profundidad (donde 1 significa el directorio actual):

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

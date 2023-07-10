---
layout: page
title: common/autoflake (español)
description: "Una herramienta para eliminar importaciones y variables no utilizadas del código Python."
content_hash: 013d42901a24725aadb2c4e932dbef618f2803b7
last_modified_at: 2023-07-10
related_topics:
  - title: English version
    url: /en/common/autoflake.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/autoflake.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/autoflake.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/autoflake.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/autoflake.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># autoflake

Una herramienta para eliminar importaciones y variables no utilizadas del código Python.
Más información: <https://github.com/myint/autoflake>.

- Elimina las variables no utilizadas de un archivo y muestra la diferencia:

`autoflake --remove-unused-variables `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.py</span>

- Elimina las importaciones no utilizadas de varios archivos y muestra las diferencias:

`autoflake --remove-all-unused-imports `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo1.py ruta/al/archivo2.py ...</span>

- Elimina variables no utilizadas de un fichero, sobrescribiendo el fichero:

`autoflake --remove-unused-variables --in-place `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.py</span>

- Elimina recursivamente las variables no utilizadas de todos los archivos de un directorio, sobrescribiendo cada archivo:

`autoflake --remove-unused-variables --in-place --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio</span>

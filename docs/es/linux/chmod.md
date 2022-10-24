---
layout: page
title: linux/chmod (español)
description: "Cambia los permisos de acceso de un archivo o directorio."
content_hash: 9efddabed4b51a8afa6c46cef03213fa9408adcd
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># chmod

Cambia los permisos de acceso de un archivo o directorio.
Más información: https://www.gnu.org/software/coreutils/chmod.

- Da al [u]suario que posee al archivo el permiso de ejecución [x]:

`chmod u+x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Da al [u]suario permisos de lectu[r]a y escritura [w] a un archivo o directorio:

`chmod u+rw `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_o_directorio</span>

- Remueve permisos de ejecución [x] del [g]rupo:

`chmod g-x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Da a todos [a] los usuarios permisos de lectu[r]a y ejecución [x]:

`chmod a+rx `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Da a [o]tros usuarios (no dentro del grupo dueño del archivo) los mismos permisos que el [g]rupo:

`chmod o=g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Remueve todos los permisos de [o]tros:

`chmod o= `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Cambia los permisos recursivamente dando al [g]rupo y a [o]tros la habilidad de escribir [w]:

`chmod -R g+w,o+w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio</span>

- Recursivamente da a todos [a] los usuarios permisos de lectu[r]a y ejecución [X] de los subdirectorios de un directorio:

`chmod -R a+rX `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio</span>

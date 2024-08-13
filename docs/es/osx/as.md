---
layout: page
title: osx/as (español)
description: "Ensamblador portable GNU."
content_hash: 4943fa626afe192b846816d0c56fa1b53d57c516
last_modified_at: 2024-08-13
related_topics:
  - title: English version
    url: /en/osx/as.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/osx/as.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/as.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/as.html
    icon: bi bi-globe
tldri18n_status: 2
---
# as

Ensamblador portable GNU.
Principalmente destinado a ensamblar la salida de `gcc` para ser utilizada por` ld`.
Más información: <https://keith.github.io/xcode-man-pages/as.1.html>.

- Ensambla un archivo, escribiendo la salida en `a.out`:

`as `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.s</span>

- Ensambla la salida a un archivo especificado:

`as `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.s</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">salida.o</span>

- Genera resultados más rápidos omitiendo los espacios en blanco y el preprocesamiento de comentarios. (Solo debe usarse para compiladores de confianza):

`as -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.s</span>

- Incluye una ruta determinada a la lista de directorios para buscar archivos especificados en las directivas `.include`:

`as -I `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.s</span>

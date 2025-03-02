---
layout: page
title: linux/as (español)
description: "Ensamblador GNU portátil."
content_hash: 83feb6d4dfea3b5311c70ccda9bd20a9dea03c96
last_modified_at: 2025-03-02
related_topics:
  - title: Deutsch version
    url: /de/linux/as.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/as.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/as.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/as.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/as.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/as.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/as.html
    icon: bi bi-globe
tldri18n_status: 2
---
# as

Ensamblador GNU portátil.
Principalmente destinado a ensamblar la salida de `gcc` para ser utilizada por `ld`.
Más información: <https://manned.org/as>.

- Ensambla un archivo, escribiendo la salida en `a.out`:

`as `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.s</span>

- Ensambla la salida en un archivo específico:

`as `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.s</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_salida.o</span>

- Genera la salida más rápida omitiendo el preprocesamiento de espacios en blanco y comentarios. (Solo debe usarse con compiladores de confianza):

`as -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.s</span>

- Incluye una ruta específica en la lista de directorios para buscar archivos especificados en las directivas `.include`:

`as -I `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.s</span>

---
layout: page
title: common/assimp (español)
description: "Cliente de línea de comandos para la biblioteca Open Asset Import."
content_hash: 61e86c3f7e9205fd445a7b5ee65064460351dbca
last_modified_at: 2024-01-07
related_topics:
  - title: English version
    url: /en/common/assimp.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/assimp.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/assimp.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/assimp.html
    icon: bi bi-globe
tldri18n_status: 2
---
# assimp

Cliente de línea de comandos para la biblioteca Open Asset Import.
Admite la carga de más de 40 formatos de archivo 3D y la exportación a varios formatos 3D populares.
Más información: <https://assimp-docs.readthedocs.io/>.

- Lista todos los formatos de importación soportados:

`assimp listext`

- Lista todos los formatos de exportación compatibles:

`assimp listexport`

- Convierte un archivo a uno de los formatos de salida soportados, utilizando los parámetros por defecto:

`assimp export `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo_entrada.stl</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo_salida.obj</span>

- Convierte un archivo utilizando parámetros personalizados (el archivo dox_cmd.h en el código fuente de assimp enumera los parámetros disponibles):

`assimp export `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo_entrada.stl</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo_salida.obj</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">parametros</span>

- Muestra un resumen del contenido de un archivo 3D:

`assimp info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Lista todos los subcomandos ("verbs") soportados:

`assimp help`

- Muestra información de ayuda sobre un subcomando concreto (por ejemplo, los parámetros específicos del mismo):

`assimp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subcomando</span>` --help`

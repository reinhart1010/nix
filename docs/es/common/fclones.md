---
layout: page
title: common/fclones (español)
description: "Eficaz buscador y eliminador de archivos duplicados."
content_hash: dae998f87634768ab3b7971a59239c8e09b9d22f
last_modified_at: 2024-04-04
related_topics:
  - title: English version
    url: /en/common/fclones.html
    icon: bi bi-globe
tldri18n_status: 2
---
# fclones

Eficaz buscador y eliminador de archivos duplicados.
Más información: <https://github.com/pkolaczk/fclones>.

- Busca ficheros duplicados en el directorio actual:

`fclones group .`

- Busca archivos duplicados en varios directorios y almacena los resultados en la caché:

`fclones group --cache `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/directorio1 ruta/a/directorio2</span>

- Busca archivos duplicados solo en el directorio especificado, omitiendo los subdirectorios y guarda los resultados en un archivo:

`fclones group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/directorio</span>` --depth 1 > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.txt</span>

- Mueve los archivos duplicados en un archivo de texto a un directorio diferente:

`fclones move `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/directorio_objetivo</span>` < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.txt</span>

- Simula un enlace simbólico a un archivo de texto sin realmente enlazarlo:

`fclones link --soft < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.txt</span>` --dry-run 2> /dev/null`

- Elimina los archivos duplicados más recientes en el directorio actual sin almacenarlos en un archivo:

`fclones group . | fclones remove --priority newest`

- Preprocesa los archivos JPEG en el directorio actual utilizando un comando externo para eliminar sus datos EXIF antes de buscar duplicados:

`fclones group . --name '*.jpg' -i --transform 'exiv2 -d a $IN' --in-place`

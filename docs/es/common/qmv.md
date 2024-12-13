---
layout: page
title: common/qmv (español)
description: "Mueve archivos y directorios usando el editor de texto predeterminado para definir los nombres de archivos."
content_hash: 20c8079850a5ef9f8fa4f67fe5bfd53403db6b02
last_modified_at: 2024-12-13
related_topics:
  - title: English version
    url: /en/common/qmv.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/qmv.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/qmv.html
    icon: bi bi-globe
tldri18n_status: 2
---
# qmv

Mueve archivos y directorios usando el editor de texto predeterminado para definir los nombres de archivos.
Más información: <https://www.nongnu.org/renameutils/>.

- Mueve un solo archivo (abre un editor con el nombre de archivo fuente a la izquierda y el nombre de archivo de destino a la derecha):

`qmv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo_original</span>

- Mueve múltiples archivos JPEG:

`qmv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.jpg</span>

- Mueve múltiples directorios:

`qmv -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio3</span>

- Mueve todos los archivos y directorios dentro de un directorio:

`qmv --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio</span>

- Mueve archivos, pero cambia las posiciones de la fuente y los nombres de archivo de destino en el editor:

`qmv --option swap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.jpg</span>

- Renombra todos los archivos y carpetas en el directorio actual, pero muestra solo los nombres de archivo de destino en el editor (puedes pensar en ello como una especie de modo simple):

`qmv --format=do .`

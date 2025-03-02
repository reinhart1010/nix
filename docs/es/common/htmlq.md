---
layout: page
title: common/htmlq (español)
description: "Utiliza selectores CSS para extraer contenido de archivos HTML."
content_hash: 294e11bc5add42fa9c8ae5488fd49e270c705821
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/htmlq.html
    icon: bi bi-globe
tldri18n_status: 2
---
# htmlq

Utiliza selectores CSS para extraer contenido de archivos HTML.
Más información: <https://github.com/mgdm/htmlq>.

- Devuelve todos los elementos de la clase `card`:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.html</span>` | htmlq '.card'`

- Obtiene el contenido del texto del primer párrafo:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.html</span>` | htmlq --text 'p:primer-del-tipo'`

- Encuentra todos los enlaces de una página:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.html</span>` | htmlq --attribute href 'a'`

- Elimina todas las imágenes y archivos SVG de una página:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.html</span>` | htmlq --remove-nodes 'img' --remove-nodes 'svg'`

- Impresión bonita y escritura de la salida en un archivo:

`htmlq --pretty --filename `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/archivo.html</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/salida.html</span>

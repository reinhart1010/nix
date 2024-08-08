---
layout: page
title: linux/filefrag (español)
description: "Informa del grado de fragmentación de un archivo en particular."
content_hash: fc1140064ba6a0a4a480291cdaca524396947d88
last_modified_at: 2024-08-08
related_topics:
  - title: English version
    url: /en/linux/filefrag.html
    icon: bi bi-globe
tldri18n_status: 2
---
# filefrag

Informa del grado de fragmentación de un archivo en particular.
Más información: <https://manned.org/filefrag>.

- Muestra un informe para uno o más archivos:

`filefrag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo1 ruta/al/archivo2 ...</span>

- Muestra un informe con un tamaño de bloque de 1024 bytes:

`filefrag -k `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Muestra un informe con un tamaño de bloque determinado:

`filefrag -b`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1024|1K|1M|1G|...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Sincroniza el archivo antes de solicitar la asignación:

`filefrag -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo1 ruta/al/archivo2 ...</span>

- Muestra la asignación de atributos extendidos:

`filefrag -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo1 ruta/al/archivo2 ...</span>

- Muestra un informe con información detallada:

`filefrag -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo1 ruta/al/archivo2 ...</span>

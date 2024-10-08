---
layout: page
title: netbsd/df (español)
description: "Muestra una visión general del uso del espacio en disco del sistema de archivos."
content_hash: 55b5800887367388e069a49697ebe0088288feba
last_modified_at: 2024-09-19
related_topics:
  - title: English version
    url: /en/netbsd/df.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/netbsd/df.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/netbsd/df.html
    icon: bi bi-globe
tldri18n_status: 2
---
# df

Muestra una visión general del uso del espacio en disco del sistema de archivos.
Más información: <https://man.netbsd.org/df.1>.

- Muestra todos los sistemas de ficheros y su uso de disco usando unidades de 512 bytes:

`df`

- Utiliza palabras [h]umanas para indicar unidades (basadas en potencias de 1024):

`df -h`

- Muestra todos los campos de la(s) estructura(s) devuelta(s) por `statvfs`:

`df -G`

- Muestra el sistema de archivos y su uso del disco que contiene el archivo o directorio dado:

`df `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_o_directorio</span>

- Incluye estadísticas sobre el número de nodos-[i] libres y utilizados:

`df -i`

- Utiliza unidades de 1024 bytes al escribir las cifras de espacio:

`df -k`

- Muestra la información de manera [P]ortable:

`df -P`

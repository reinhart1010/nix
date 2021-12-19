---
layout: page
title: linux/clamav (español)
description: "Antivirus de código abierto."
content_hash: 0ccd6f91f19859a8293ec37ca6f5cf14e1221836
related_topics:
  - title: English version
    url: /en/linux/clamav.html
    icon: bi bi-globe
---
# clamav

Antivirus de código abierto.
Diseñado especialment para escanear correos electrónicos, pero puede ser usado en otros contextos.
Más información: <https://www.clamav.net>.

- Actualiza definiciones de virus:

`freshclam`

- Escanea un archivo en busca de virus:

`clamscan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Escanea directorios recursivamente y mostrar los archivos infectados:

`clamscan --recursive --infected `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio</span>

- Escanea directorios recursivamente y poner los archivos infectados en cuarentena:

`clamscan --recursive --move=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">directorio</span>

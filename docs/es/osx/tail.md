---
layout: page
title: osx/tail (español)
description: "Muestra la última parte de un archivo."
content_hash: 67019796f8dec6b10ea2c5aedd0385c6b1a5c4d0
last_modified_at: 2024-09-28
related_topics:
  - title: English version
    url: /en/osx/tail.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/osx/tail.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tail

Muestra la última parte de un archivo.
Vea también: `head`.
Más información: <https://keith.github.io/xcode-man-pages/tail.1.html>.

- Muestra las últimas líneas 'count' del archivo:

`tail -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Imprime un archivo a partir de un número de línea específico:

`tail -n +`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Imprime un recuento específico de bytes desde el final de un archivo determinado:

`tail -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Imprime las últimas líneas de un archivo dado y sigue leyéndolo hasta `Ctrl + C`:

`tail -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Sigue leyendo el archivo hasta `Ctrl + C`, incluso si el archivo es inaccesible:

`tail -F `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Muestra las últimas líneas 'contadas' en 'archivo' y lo actualiza cada 'n' segundos:

`tail -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8</span>` -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

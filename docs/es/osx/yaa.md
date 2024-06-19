---
layout: page
title: osx/yaa (español)
description: "Crea y manipula archivos YAA."
content_hash: 970e57879978ca90aabe0e52fa269594d4e43293
last_modified_at: 2024-06-19
related_topics:
  - title: English version
    url: /en/osx/yaa.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/osx/yaa.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/osx/yaa.html
    icon: bi bi-globe
tldri18n_status: 2
---
# yaa

Crea y manipula archivos YAA.
Más información: <https://keith.github.io/xcode-man-pages/yaa.1.html>.

- Crea un archivo a partir de un directorio:

`yaa archive -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_de_salida.yaa</span>

- Crea un archivo a partir de un fichero:

`yaa archive -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_de_salida.yaa</span>

- Extrae un archivo al directorio actual:

`yaa extract -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.yaa</span>

- Lista el contenido de un archivo:

`yaa list -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.yaa</span>

- Crea un archivo con un algoritmo de compresión específico:

`yaa archive -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">algorithm</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_de_salida.yaa</span>

- Crea un archivo con un tamaño de bloque de 8 MB:

`yaa archive -b 8m -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_de_salida.yaa</span>

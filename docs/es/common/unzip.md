---
layout: page
title: common/unzip (español)
description: "Extrae archivos/directorios de archivos Zip."
content_hash: 2a1f1247afd124f5e1b0b6383aa0b13a62b72b20
last_modified_at: 2024-12-21
related_topics:
  - title: English version
    url: /en/common/unzip.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/unzip.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/unzip.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/unzip.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/unzip.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/unzip.html
    icon: bi bi-globe
tldri18n_status: 2
---
# unzip

Extrae archivos/directorios de archivos Zip.
Vea también: `zip`.
Más información: <https://manned.org/unzip>.

- Extrae todos los archivos/directorios de archivos específicos en el directorio actual:

`unzip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo1.zip ruta/al/archivo2.zip ...</span>

- Extrae los archivos/directorios de archivos a una ruta específica:

`unzip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo1.zip ruta/al/archivo2.zip ...</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/resultado</span>

- Extrae los archivos/directorios de archivos a `stdout` junto con los nombres de archivos extraídos:

`unzip -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo1.zip ruta/al/archivo2.zip ...</span>

- Extrae un archivo creado en Windows, que contiene archivos con caracteres no ASCII en su nombre (por ejemplo, caracteres chinos o japoneses):

`unzip -O `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gbk</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo1.zip ruta/al/archivo2.zip ...</span>

- Enumera los contenidos de un archivo específico sin extraerlos:

`unzip -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.zip</span>

- Extrae un archivo específico de un archivo:

`unzip -j `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.zip</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo1_en_archivo ruta/al/archivo2_en_archivo ...</span>

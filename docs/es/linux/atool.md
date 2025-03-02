---
layout: page
title: linux/atool (español)
description: "Administra archivos comprimidos en varios formatos."
content_hash: 72b9639de5bef1c999d95994860ee78ade96f287
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/linux/atool.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/atool.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/atool.html
    icon: bi bi-globe
tldri18n_status: 2
---
# atool

Administra archivos comprimidos en varios formatos.
Más información: <https://www.nongnu.org/atool/>.

- Muestra los archivos dentro de un archivo Zip:

`atool --list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.zip</span>

- Extrae un archivo tar.gz en un nuevo subdirectorio (o en el directorio actual si contiene solo un archivo):

`atool --extract `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.tar.gz</span>

- Crea un nuevo archivo 7z con dos archivos:

`atool --add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.7z</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo1 ruta/al/archivo2 ...</span>

- Extrae todos los archivos Zip y rar en el directorio actual:

`atool --each --extract `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.zip *.rar</span>

---
layout: page
title: common/7zr (español)
description: "Archivador de ficheros con un alto ratio de compresión."
content_hash: 193994c485377932dc14c39d479dfa25413a9224
last_modified_at: 2024-03-14
related_topics:
  - title: বাংলা version
    url: /bn/common/7zr.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/common/7zr.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/7zr.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/7zr.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/7zr.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/7zr.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/7zr.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/7zr.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/7zr.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/7zr.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/7zr.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/7zr.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/common/7zr.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/7zr.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/7zr.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># 7zr

Archivador de ficheros con un alto ratio de compresión.
Similar a `7z` excepto que sólo soporta ficheros 7z.
Más información: <https://manned.org/7zr>.

- [a]rchiva un archivo o directorio:

`7zr a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.7z</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_o_directorio</span>

- Cifra un archivo existente (incluidos los nombres de los archivos):

`7zr a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.7z</span>` -p`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">contraseña</span>` -mhe=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">on</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.7z</span>

- E[x]trae un archivo conservando la estructura de directorios original:

`7zr x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.7z</span>

- E[x]trae un archivo a un directorio específico:

`7zr x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.7z</span>` -o{ruta/de/salida</span>

- E[x]trae un archivo a `stdout`:

`7zr x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.7z</span>` -so`

- [l]ista el contenido de un archivo:

`7zr l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.7z</span>

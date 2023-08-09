---
layout: page
title: osx/md5 (español)
description: "Calcula sumas de comprobación criptográficas MD5."
content_hash: cce8f9635c609b142923e53213af70d56a0c41f0
last_modified_at: 2023-08-09
related_topics:
  - title: Deutsch version
    url: /de/osx/md5.html
    icon: bi bi-globe
  - title: English version
    url: /en/osx/md5.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/md5.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># md5

Calcula sumas de comprobación criptográficas MD5.
Más información: <https://ss64.com/osx/md5.html>.

- Calcula la suma de comprobación MD5 de un archivo:

`md5 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Calcula sumas de comprobación MD5 para varios archivos:

`md5 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo1 ruta/al/archivo2 ...</span>

- Obtiene sólo la suma de comprobación md5 (sin nombre de archivo):

`md5 -q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Imprime una suma de comprobación de la cadena dada:

`md5 -s "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cadena</span>`"`

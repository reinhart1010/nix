---
layout: page
title: common/xz (español)
description: "Comprime o descomprime archivos XZ y LZMA."
content_hash: ae9d6c5a6755067a35129bb9af2b2fdc65270ff5
last_modified_at: 2024-10-31
related_topics:
  - title: English version
    url: /en/common/xz.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/xz.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/xz.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/xz.html
    icon: bi bi-globe
tldri18n_status: 2
---
# xz

Comprime o descomprime archivos XZ y LZMA.
Más información: <https://manned.org/xz>.

- Comprime un archivo usando xz:

`xz `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Descomprime un archivo XZ:

`xz --decompress `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.xz</span>

- Comprime un archivo usando LZMA:

`xz --format=lzma `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Descomprime un archivo LZMA:

`xz --decompress --format=lzma `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.lzma</span>

- Descomprime un archivo y escribe a `stdout` (implica `--keep`):

`xz --decompress --stdout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.xz</span>

- Comprime un archivo, pero no borra el original:

`xz --keep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Comprime un archivo con la compresión más rápida:

`xz -0 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Comprime un archivo con la mejor compresión:

`xz -9 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

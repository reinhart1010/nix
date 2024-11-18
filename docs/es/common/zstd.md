---
layout: page
title: common/zstd (español)
description: "Comprime o descomprime archivos con compresión Zstandard."
content_hash: 4732465b716227582e37852e34905f5a67e50782
last_modified_at: 2024-11-18
related_topics:
  - title: English version
    url: /en/common/zstd.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/zstd.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/zstd.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/zstd.html
    icon: bi bi-globe
tldri18n_status: 2
---
# zstd

Comprime o descomprime archivos con compresión Zstandard.
Más información: <https://github.com/facebook/zstd>.

- Comprime un archivo en un nuevo archivo con el sufijo `.zst`:

`zstd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Descomprime un archivo:

`zstd --decompress `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.zst</span>

- Descomprime a la salida estándar `stdout`:

`zstd --decompress --stdout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.zst</span>

- Comprime un archivo especificando el nivel de compresión, donde 1=más rápido, 19=más lento y 3=predeterminado:

`zstd -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nivel</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Desbloquea niveles de compresión superiores (hasta 22) utilizando más memoria (tanto para compresión como descompresión):

`zstd --ultra -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nivel</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

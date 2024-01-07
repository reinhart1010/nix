---
layout: page
title: common/mid3v2 (español)
description: "Edita etiquetas de audio."
content_hash: 92f1b5c64f3943d7924145a41355364eb3d71b65
last_modified_at: 2024-01-07
related_topics:
  - title: English version
    url: /en/common/mid3v2.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mid3v2

Edita etiquetas de audio.
Vea también: `id3v2`.
Más información: <https://manned.org/mid3v2.1>.

- Lista de todos los marcos ID3v2.3 o ID3v2.4 admitidos y sus significados:

`id3v2 --list-frames `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo1.mp3 ruta/al/archivo2.mp3 ...</span>

- Lista de todos los géneros numéricos ID3v1 admitidos:

`id3v2 --list-genres `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo1.mp3 ruta/al/archivo2.mp3 ...</span>

- Lista todas las etiquetas en archivos específicos:

`id3v2 --list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo1.mp3 ruta/al/archivo2.mp3 ...</span>

- Establece información específica sobre artistas, álbumes o canciones:

`id3v2 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--artist|--album|--song</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo1.mp3 ruta/al/archivo2.mp3 ...</span>

- Establece información específica de la imagen:

`id3v2 --picture=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename:description:image_type:mime_type</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo1.mp3 ruta/al/archivo2.mp3 ...</span>

- Establece información específica del año:

`id3v2 --year=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">YYYY</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo1.mp3 ruta/al/archivo2.mp3 ...</span>

- Establece información de fecha específica:

`id3v2 --date=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">YYYY-MM-DD</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo1.mp3 ruta/al/archivo2.mp3 ...</span>

---
layout: page
title: common/audtool (español)
description: "Controla Audacious usando comandos."
content_hash: be1af131f3955fbe3b25cb6dfcfdf4f2e3775b86
last_modified_at: 2024-06-06
related_topics:
  - title: English version
    url: /en/common/audtool.html
    icon: bi bi-globe
tldri18n_status: 2
---
# audtool

Controla Audacious usando comandos.
Más información: <https://manned.org/audtool>.

- Reproduce/pausa la reproducción de audio:

`audtool playback-playpause`

- Imprime el nombre del artista, el álbum y la canción que se está reproduciendo:

`audtool current-song`

- Ajusta el volumen de la reproducción de audio:

`audtool set-volume `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>

- Salta a la siguiente canción:

`audtool playlist-advance`

- Imprime la tasa de bits de la canción actual en kilobits:

`audtool current-song-bitrate-kbps`

- Abre Audacious en pantalla completa si está oculto:

`audtool mainwin-show`

- Muestra ayuda:

`audtool help`

- Muestra configuración:

`audtool preferences-show`

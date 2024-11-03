---
layout: page
title: common/audacious (español)
description: "Un reproductor de audio de código abierto. Basado indirectamente en XMMS."
content_hash: 56f1ee577bb9dace6003d8f8442beec9175a2c84
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/common/audacious.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/audacious.html
    icon: bi bi-globe
tldri18n_status: 2
---
# audacious

Un reproductor de audio de código abierto. Basado indirectamente en XMMS.
Vea también: `audtool`, `clementine`, `mpc`, `ncmpcpp`.
Más información: <https://audacious-media-player.org>.

- Inicia la interfaz gráfica:

`audacious`

- Inicia una nueva instancia y reproduce un audio:

`audacious --new-instance `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/audio</span>

- Pone en cola un directorio específico de archivos de audio:

`audacious --enqueue `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio</span>

- Inicia o detiene la reproducción:

`audacious --play-pause`

- Salta hacia delante ([fwd]) o hacia atrás ([rew]) en la lista de reproducción:

`audacious --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fwd|rew</span>

- Detiene la reproducción:

`audacious --stop`

- Inicia en modo CLI (headless):

`audacious --headless`

- Sale en cuanto se detenga la reproducción o no haya nada que reproducir:

`audacious --quit-after-play`

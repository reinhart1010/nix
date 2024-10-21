---
layout: page
title: common/pactl (español)
description: "Controla un servidor de sonido PulseAudio en ejecución."
content_hash: cf22e8a3ca2b467b86246be7e11c98311ef3cfcd
last_modified_at: 2024-10-21
related_topics:
  - title: English version
    url: /en/common/pactl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pactl

Controla un servidor de sonido PulseAudio en ejecución.
Más información: <https://manned.org/pactl>.

- Muestra información sobre el servidor de sonido:

`pactl info`

- Lista todos los sinks (u otros tipos - los sinks son salidas y los sink-inputs son flujos de audio activos):

`pactl list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sinks</span>` short`

- Cambia el sink (salida) predeterminado a 1 (el número se puede obtener mediante el subcomando `list`):

`pactl set-default-sink `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>

- Mueve el sink-input 627 al sink 1:

`pactl move-sink-input `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">627</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>

- Establece el volumen del sink 1 al 75%:

`pactl set-sink-volume `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0.75</span>

- Cambia el estado de silencio del sink predeterminado (usando el nombre especial `@DEFAULT_SINK@`):

`pactl set-sink-mute `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">@DEFAULT_SINK@</span>` toggle`

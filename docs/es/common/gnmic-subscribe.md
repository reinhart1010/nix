---
layout: page
title: common/gnmic-subscribe (español)
description: "Suscribirse a las actualizaciones de estado de un dispositivo de red gnmic."
content_hash: 409b8fd560bcbe2f9782e0555ebf0323c314122e
last_modified_at: 2024-12-01
related_topics:
  - title: English version
    url: /en/common/gnmic-subscribe.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/gnmic-subscribe.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/gnmic-subscribe.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gnmic subscribe

Suscribirse a las actualizaciones de estado de un dispositivo de red gnmic.
Más información: <https://gnmic.kmrd.dev/cmd/subscribe>.

- Suscribirse a las actualizaciones del estado objetivo bajo el subárbol de una ruta específica:

`gnmic --address `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip:puerto</span>` subscribe --path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta</span>

- Suscribirse a un objetivo con un intervalo de muestra de 30s (por defecto es 10s):

`gnmic -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip:puerto</span>` subscribe --path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta</span>` --sample-interval 30s`

- Suscribirse a un objetivo con intervalo de muestra y actualizaciones solamente cuando hay cambios:

`gnmic -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip:puerto</span>` subscribe --path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta</span>` --stream-mode on-change --heartbeat-interval 1m`

- Suscribirse a un objetivo para una sola actualización:

`gnmic -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip:puerto</span>` subscribe --path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta</span>` --mode once`

- Suscribirse a un objetivo y especificar la codificación de la respuesta (json_ietf):

`gnmic -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip:puerto</span>` subscribe --path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta</span>` --encoding json_ietf`

---
layout: page
title: common/asciinema (español)
description: "Graba y reproduce sesiones de terminal, y opcionalmente compártelas en asciinema.org."
content_hash: 8d330c5d2d7f0c2bfdfee43a2726fce2d1efecf1
last_modified_at: 2024-05-22
related_topics:
  - title: English version
    url: /en/common/asciinema.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/asciinema.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/asciinema.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/asciinema.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/asciinema.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/asciinema.html
    icon: bi bi-globe
tldri18n_status: 2
---
# asciinema

Graba y reproduce sesiones de terminal, y opcionalmente compártelas en asciinema.org.
Más información: <https://docs.asciinema.org/manual/cli/usage>.

- Asocia el programa local de `asciinema` con una cuenta de asciinema.org:

`asciinema auth`

- Crea una nueva grabación (una vez acabada, se preguntará al usuario si la quiere guardar en local, o subirla):

`asciinema rec`

- Crea una nueva grabación y la guarda en un archivo local:

`asciinema rec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/hacia/grabación.cast</span>

- Reproduce una grabación desde un archivo local:

`asciinema play `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/hacia/grabación.cast</span>

- Reproduce una grabación desde asciinema.org:

`asciinema play https://asciinema.org/a/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">identificador_de_grabación</span>

- Crea una nueva grabación, limitando el tiempo de espera máximo a 2.5 segundos:

`asciinema rec -i 2.5`

- Imprime la salida completa de un archivo local de grabación:

`asciinema cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/hacia/grabación.cast</span>

- Sube un archivo local de grabación a asciinema.org:

`asciinema upload `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/hacia/grabación.cast</span>

---
layout: page
title: common/asciinema (español)
description: "Graba y reproduce sesiones de terminal, y opcionalmente compártelas en asciinema.org."
content_hash: 7133512459f39d1df6dbf4fb374bc17141689072
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
---
# asciinema

Graba y reproduce sesiones de terminal, y opcionalmente compártelas en asciinema.org.
Más información: <https://asciinema.org/>.

- Asocia el programa local de `asciinema` con una cuenta de asciinema.org:

`asciinema auth`

- Crea una nueva grabación (una vez acabada, se preguntará al usuario si la quiere guardar en local, o subirla):

`asciinema rec`

- Crea una nueva grabación y la guarda en un archivo local:

`asciinema rec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/hacia/archivo</span>`.cast`

- Reproduce una grabación desde un archivo local:

`asciinema play `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/hacia/archivo</span>`.cast`

- Reproduce una grabación desde asciinema.org:

`asciinema play https://asciinema.org/a/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cast_id</span>

- Crea una nueva grabación, limitando el tiempo de espera máximo a 2.5 segundos:

`asciinema rec -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2.5</span>

- Imprime la salida completa de un archivo local de grabación:

`asciinema cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/hacia/archivo</span>`.cast`

- Sube un archivo local de grabación a asciinema.org:

`asciinema upload `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/hacia/archivo</span>`.cast`

---
layout: page
title: osx/afplay (español)
description: "Reproductor de audio de línea de comandos."
content_hash: d0ec035e1483f16f75bb1211adfcca44dbe5c09b
last_modified_at: 2024-01-31
related_topics:
  - title: English version
    url: /en/osx/afplay.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/osx/afplay.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/afplay.html
    icon: bi bi-globe
tldri18n_status: 2
---
# afplay

Reproductor de audio de línea de comandos.
Más información: <https://keith.github.io/xcode-man-pages/afplay.1.html>.

- Reproduce un archivo de audio (espera hasta que finalice la reproducción):

`afplay `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Reproduce un archivo de audio a una velocidad 2x (velocidad de reproducción):

`afplay --rate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Reproduce un archivo de audio a la mitad de velocidad:

`afplay --rate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0.5</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Reproduce los primeros N segundos de un archivo de audio:

`afplay --time `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">segundos</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

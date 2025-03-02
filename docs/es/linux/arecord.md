---
layout: page
title: linux/arecord (español)
description: "Grabadora de sonido para el controlador de tarjeta de sonido ALSA."
content_hash: 5bbc83a577526ed2b2fb80f15760fd964be05672
last_modified_at: 2025-03-02
related_topics:
  - title: Deutsch version
    url: /de/linux/arecord.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/arecord.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/arecord.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/arecord.html
    icon: bi bi-globe
tldri18n_status: 2
---
# arecord

Grabadora de sonido para el controlador de tarjeta de sonido ALSA.
Más información: <https://manned.org/arecord>.

- Graba un fragmento en calidad "CD" (finaliza con Ctrl-C cuando termines):

`arecord -vv --format=cd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.wav</span>

- Graba un fragmento en calidad "CD", con una duración fija de 10 segundos:

`arecord -vv --format=cd --duration=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.wav</span>

- Graba un fragmento y lo guarda como MP3 (finaliza con Ctrl-C cuando termines):

`arecord -vv --format=cd --file-type raw | lame -r - `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.mp3</span>

- Muestra todas las tarjetas de sonido y dispositivos de audio digital:

`arecord --list-devices`

- Permite una interfaz interactiva (por ejemplo, usa la barra espaciadora o tecla Entrar para reproducir o pausar):

`arecord --interactive`

- Prueba tu micrófono grabando una muestra de 5 segundos y reproduciéndola:

`arecord -d 5 test-mic.wav && aplay test-mic.wav && rm test-mic.wav`

---
layout: page
title: linux/shnsplit (español)
description: "Divide archivos de audio según un archivo `.cue`."
content_hash: 3d22ed84c3159b62907c303e7f7d3e9c7e3765c9
last_modified_at: 2024-11-18
related_topics:
  - title: English version
    url: /en/linux/shnsplit.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/shnsplit.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/shnsplit.html
    icon: bi bi-globe
tldri18n_status: 2
---
# shnsplit

Divide archivos de audio según un archivo `.cue`.
Más información: <http://shnutils.freeshell.org/shntool/>.

- Divide un archivo `.wav` + `.cue` en múltiples archivos:

`shnsplit -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.cue</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.wav</span>

- Muestra formatos compatibles:

`shnsplit -a`

- Divide un archivo `.flac` en varios archivos:

`shnsplit -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.cue</span>` -o flac `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.flac</span>

- Divide un archivo `.wav` en archivos de la forma "número-de-pista - álbum - título":

`shnsplit -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.cue</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.wav</span>` -t "%n - %a - %t"`

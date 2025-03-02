---
layout: page
title: linux/aplay (español)
description: "Reproductor de sonido para el controlador de tarjeta de sonido ALSA."
content_hash: 5557d283c282ba301fb6c4d517c0641bf92ad334
last_modified_at: 2025-03-02
related_topics:
  - title: Deutsch version
    url: /de/linux/aplay.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/aplay.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/aplay.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/aplay.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/aplay.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aplay

Reproductor de sonido para el controlador de tarjeta de sonido ALSA.
Más información: <https://manned.org/aplay>.

- Reproduce un archivo específico (la tasa de muestreo, la profundidad de bits, etc. se determinarán automáticamente según el formato del archivo):

`aplay `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Reproduce los primeros 10 segundos de un archivo específico a 2500 Hz:

`aplay --duration=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` --rate=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2500</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Reproduce el archivo en formato sin procesar como un archivo `.au` de 22050 Hz, mono, 8 bits, Mu-Law:

`aplay --channels=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` --file-type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">raw</span>` --rate=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">22050</span>` --format=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mu_law</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

---
layout: page
title: osx/nvram (español)
description: "Manipula variables del firmware."
content_hash: 05481b462c8bc60bfe9def3ee63eb7db7124e67c
last_modified_at: 2024-01-31
related_topics:
  - title: English version
    url: /en/osx/nvram.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nvram

Manipula variables del firmware.
Más información: <https://keith.github.io/xcode-man-pages/nvram.8.html>.

- Im[p]rime todas las variables almacenadas en la NVRAM:

`nvram -p`

- Im[p]rime todas las variables almacenadas en la NVRAM usando el formato [x]ML:

`nvram -xp`

- Modifica el valor de una variable del firmware:

`sudo nvram `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre</span>`="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">valor</span>`"`

- Elimina una variable de firmware:

`sudo nvram -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre</span>

- [c]larifica todas las variables de firmware:

`sudo nvram -c`

- Establece una variable de firmware de un [x]ML [f]ile específico:

`sudo nvram -xf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.xml</span>

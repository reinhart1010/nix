---
layout: page
title: osx/nvram (español)
description: "Manipula variables del firmware."
content_hash: 7ed3acfbd6b11b3b991ce94a2841f0bd6113e7f7
last_modified_at: 2023-08-09
related_topics:
  - title: English version
    url: /en/osx/nvram.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># nvram

Manipula variables del firmware.
Más información: <https://ss64.com/osx/nvram.html>.

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

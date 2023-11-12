---
layout: page
title: common/avrdude (español)
description: "Programa controlador para la programación de microcontroladores Atmel AVR."
content_hash: e4685bd73da3b2f82a17fa626a753520b7525ca0
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/avrdude.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/avrdude.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/avrdude.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/avrdude.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/avrdude.html
    icon: bi bi-globe
tldri18n_status: 2
---
# avrdude

Programa controlador para la programación de microcontroladores Atmel AVR.
Más información: <https://www.nongnu.org/avrdude/>.

- Lee el microcontrolador AVR:

`avrdude -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">AVR_dispositivo</span>` -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">programador</span>` -U flash:r:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.hex</span>`:i`

- Escribe el microcontrolador AVR:

`avrdude -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">AVR_dispositivo</span>` -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">programador</span>` -U flash:w:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.hex</span>

- Lista de dispositivos AVR disponibles:

`avrdude -p \?`

- Lista de programadores AVR disponibles:

`avrdude -c \?`

---
layout: page
title: common/avrdude (italiano)
description: "Driver per il programmatore di microcontrollori Atmel AVR."
content_hash: 2ca9330896ed2a9b0e07658a082ccfeab8daf3e4
related_topics:
  - title: Deutsch version
    url: /de/common/avrdude.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/avrdude.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/avrdude.html
    icon: bi bi-globe
---
# avrdude

Driver per il programmatore di microcontrollori Atmel AVR.
Maggiori informazioni: <https://www.nongnu.org/avrdude/>.

- Leggi dal microcontrollore AVR:

`avrdude -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dispositivo_AVR</span>` -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_programmatore</span>` -U flash:r:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.hex</span>`:i`

- Scrivi sul microcontrollore AVR:

`avrdude -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dispositivo_AVR</span>` -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_programmatore</span>` -U flash:w:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.hex</span>

- Elenca dispositivi AVR disponibili:

`avrdude -p \?`

- Elenca programmatori AVR disponibili:

`avrdude -c \?`

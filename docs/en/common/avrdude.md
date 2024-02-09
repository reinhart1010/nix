---
layout: page
title: common/avrdude (English)
description: "Driver program for Atmel AVR microcontrollers programming."
content_hash: b2106bfccae2e0557722aa1a4e4bba15af80de7d
last_modified_at: 2024-02-09
related_topics:
  - title: Deutsch version
    url: /de/common/avrdude.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/avrdude.html
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

Driver program for Atmel AVR microcontrollers programming.
More information: <https://www.nongnu.org/avrdude/>.

- [r]ead the flash ROM of a AVR microcontroller with a specific [p]art id:

`avrdude -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">part_no</span>` -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">programmer_id</span>` -U flash:r:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.hex</span>`:i`

- [w]rite to the flash ROM AVR microcontroller:

`avrdude -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">part_no</span>` -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">programmer</span>` -U flash:w:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.hex</span>

- List available AVR devices:

`avrdude -p \?`

- List available AVR programmers:

`avrdude -c \?`

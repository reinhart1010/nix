---
layout: page
title: common/avrdude (Deutsch)
description: "Treiberprogramm für Atmel AVR Mikrocontroller-Programmierung."
content_hash: b98354b85702a312079e9d1232e2235b29b3d213
related_topics:
  - title: English version
    url: /en/common/avrdude.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/avrdude.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/avrdude.html
    icon: bi bi-globe
---
# avrdude

Treiberprogramm für Atmel AVR Mikrocontroller-Programmierung.
Weitere Informationen: <https://www.nongnu.org/avrdude/>.

- Schreibt den Speicherinhalt eines AVR-Mikrocontrollers in eine Datei:

`avrdude -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">avr_gerät</span>` -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">programmer</span>` -U flash:r:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei.hex</span>`:i`

- Schreibt den Inhalt einer Datei in einen AVR-Mikrocontroller:

`avrdude -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">avr_gerät</span>` -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">programmer</span>` -U flash:w:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei.hex</span>

- Liste alle verfügbaren AVR-Geräte auf:

`avrdude -p \?`

- Liste alle verfügbaren AVR-Programmer auf:

`avrdude -c \?`

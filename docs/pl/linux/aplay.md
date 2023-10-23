---
layout: page
title: linux/aplay (polski)
description: "Konsolowy odtwarzacz dźwięku dla drivera dźwiękowego ALSA."
content_hash: b675b0b22d5d5a7302072925ec4e3bf364e132ce
last_modified_at: 2023-10-23
related_topics:
  - title: Deutsch version
    url: /de/linux/aplay.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/aplay.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/aplay.html
    icon: bi bi-globe
---
# aplay

Konsolowy odtwarzacz dźwięku dla drivera dźwiękowego ALSA.
Więcej informacji: <https://manned.org/aplay>.

- Odtwórz określony plik (częstotliwość próbkowania, ilość bitów, itd. będą określone automatycznie na podstawie formatu):

`aplay `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku</span>

- Odtwórz pierwsze 10 sekund określonego pliku z częstotliwością 2500 Hz::

`aplay --duration=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` --rate=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2500</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku</span>

- Odtwórz surowy plik jako plik `.au` 22050 Hz, mono, 8-bit, Mu-Law:

`aplay --channels=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` --file-type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">raw</span>` --rate=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">22050</span>` --format=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mu_law</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku</span>

---
layout: page
title: linux/aplay (polski)
description: "Konsolowy odtwarzacz dźwięku dla sterownika dźwiękowego ALSA."
content_hash: 51d32f398dc7bcb632bba1900c476623afd0b13a
last_modified_at: 2023-11-12
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
tldri18n_status: 2
---
# aplay

Konsolowy odtwarzacz dźwięku dla sterownika dźwiękowego ALSA.
Więcej informacji: <https://manned.org/aplay>.

- Odtwórz określony plik (częstotliwość próbkowania, ilość bitów, itd. będą określane automatycznie na podstawie formatu):

`aplay `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku</span>

- Odtwórz pierwsze 10 sekund określonego pliku z częstotliwością 2500 Hz:

`aplay --duration=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` --rate=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2500</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku</span>

- Odtwórz surowy plik jako plik Mu-Law `.au`, 22050 Hz, mono, 8-bit:

`aplay --channels=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` --file-type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">raw</span>` --rate=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">22050</span>` --format=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mu_law</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku</span>

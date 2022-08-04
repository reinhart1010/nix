---
layout: page
title: linux/pulseaudio (italiano)
description: "Programma che permette di gestire il daemon audio di sistema."
content_hash: 7565c6f2f3ccd66cf9823e9d351b2754c67fed72
related_topics:
  - title: English version
    url: /en/linux/pulseaudio.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/pulseaudio.html
    icon: bi bi-globe
---
# pulseaudio

Programma che permette di gestire il daemon audio di sistema.
Maggiori informazioni: <https://www.freedesktop.org/wiki/Software/PulseAudio/>.

- Controlla se PulseAudio è in esecuzione. Se il programma non è attivo viene restituito un exit code diverso da 0:

`pulseaudio --check`

- Esegue il daemon di PulseAudio in background:

`pulseaudio --start`

- Interrompe l'esecuzione del daemon di PulseAudio:

`pulseaudio --kill`

- Mostra i moduli disponibili:

`pulseaudio --dump-modules`

- Carica un modulo all'interno del daemon in esecuzione con gli argomenti specificati:

`pulseaudio --load="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_modulo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">argomenti</span>`"`

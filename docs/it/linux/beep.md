---
layout: page
title: linux/beep (italiano)
description: "Un'utilità per emettere un segnale acustico all'altoparlante del PC."
content_hash: 08ff15ddea45d9e8b0f73ec22871e9321f9e57ef
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/linux/beep.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/beep.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/beep.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/beep.html
    icon: bi bi-globe
tldri18n_status: 2
---
# beep

Un'utilità per emettere un segnale acustico all'altoparlante del PC.
Maggiori informazioni: <https://github.com/spkr-beep/beep>.

- Emetti un suono:

`beep`

- Emetti un suono che si ripete:

`beep -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ripetizioni</span>

- Emetti un suono a una specifica frequenza (Hz) e durata (millisecondi):

`beep -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">frequenza</span>` -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">durata</span>

- Riproduci ogni nuova frequenza e durata come un segnale acustico distinto:

`beep -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">frequenza</span>` -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">durata</span>` -n -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">frequenza</span>` -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">durata</span>

- Suona la scala di do maggiore:

`beep -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">262</span>` -n -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">294</span>` -n -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">330</span>` -n -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">349</span>` -n -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">392</span>` -n -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">440</span>` -n -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">494</span>` -n -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">523</span>

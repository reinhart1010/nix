---
layout: page
title: linux/radeontop (italiano)
description: "Mostra Utilizzo di AMD GPUs."
content_hash: 1e7e48b96352ce21d7f7bf19999cb03ef8e5126a
related_topics:
  - title: English version
    url: /en/linux/radeontop.html
    icon: bi bi-globe
---
# radeontop

Mostra Utilizzo di AMD GPUs.
Maggiori informazioni: <https://github.com/clbr/radeontop>.

- Mostra utilizzo del AMD GPU principale:

`sudo radeontop`

- Inizia output con colore:

`sudo radeontop --colour`

- Scegli un GPU specifico (il numero del bus è il primo numero nell'output di `lspci`):

`sudo radeontop --bus `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bus_numero</span>

- Specifica la frequenza di aggiornamento del display (più alto aggiunge più sovraccarico al GPU):

`sudo radeontop --ticks `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">aggiornamenti_per_secondo</span>

---
layout: page
title: linux/radeontop (italiano)
description: "Mostra Utilizzo di AMD GPUs."
content_hash: 92624988196006fe929ab8ff00ce0bf86f5201af
last_modified_at: 2023-12-29
related_topics:
  - title: English version
    url: /en/linux/radeontop.html
    icon: bi bi-globe
tldri18n_status: 2
---
# radeontop

Mostra Utilizzo di AMD GPUs.
Maggiori informazioni: <https://github.com/clbr/radeontop>.

- Mostra utilizzo del AMD GPU principale:

`radeontop`

- Inizia output con colore:

`radeontop --color`

- Scegli un GPU specifico (il numero del bus è il primo numero nell'output di `lspci`):

`radeontop --bus `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bus_numero</span>

- Specifica la frequenza di aggiornamento del display (più alto aggiunge più sovraccarico al GPU):

`radeontop --ticks `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">aggiornamenti_per_secondo</span>

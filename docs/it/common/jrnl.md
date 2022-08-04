---
layout: page
title: common/jrnl (italiano)
description: "Una semplice applicazione da linea di comando per tenere un diario."
content_hash: b40a318c1c29bd5d4e67bc6adf8988660e31db5e
related_topics:
  - title: English version
    url: /en/common/jrnl.html
    icon: bi bi-globe
---
# jrnl

Una semplice applicazione da linea di comando per tenere un diario.
Maggiori informazioni: <http://jrnl.sh>.

- Inserisci una nuova nota con il tuo editor:

`jrnl`

- Inserimento veloce di una nota:

`jrnl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">today at 3am</span>`: `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">titolo</span>`. `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">contenuto</span>

- Mostra le ultime dieci note inserite:

`jrnl -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>

- Mostra tutto quello che è successo dall'inizio dello scorso anno fino all'inizio di marzo:

`jrnl -from "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">last year</span>`" -until `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">march</span>

- Modifica tutte le note taggate con "texas" e "history":

`jrnl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">@texas</span>` -and `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">@history</span>` --edit`

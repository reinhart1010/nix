---
layout: page
title: common/asciinema (italiano)
description: "Registra e riproduci sessioni di terminale, condividendole opzionalmente su asciiname.org."
content_hash: f3e39e6dd87fafe612de5cda056f2d0438e51aed
last_modified_at: 2024-09-25
related_topics:
  - title: English version
    url: /en/common/asciinema.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/asciinema.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/asciinema.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/asciinema.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/asciinema.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/asciinema.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/asciinema.html
    icon: bi bi-globe
tldri18n_status: 2
---
# asciinema

Registra e riproduci sessioni di terminale, condividendole opzionalmente su asciiname.org.
Maggiori informazioni: <https://docs.asciinema.org/manual/cli/usage>.

- Associa l'installazione locale di `asciiname` ad un account di asciiname.org:

`asciinema auth`

- Avvia una nuova registrazione (una volta terminata, verrà chiesto se caricarla o salvarla localmente):

`asciinema rec`

- Avvia una nuova registrazione e salvala come file locale:

`asciinema rec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/registrazione.cast</span>

- Riproduci una sessione da un file locale:

`asciinema play `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/registrazione.cast</span>

- Riproducei una sessione da asciinema.org:

`asciinema play https://asciinema.org/a/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_registrazione</span>

- Avvia una nuova registrazione, limitando qualsiasi periodo di [i]nattività a 2.5 secondi:

`asciinema rec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-i|--idle-time-limit</span>` 2.5`

- Stampa l'output completo di una sessione locale:

`asciinema cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/registrazione.cast</span>

- Carica una sessione locale su asciinama.org:

`asciinema upload `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/registrazione.cast</span>

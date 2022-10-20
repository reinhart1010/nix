---
layout: page
title: common/asciinema (italiano)
description: "Registra e riproduci sessioni di terminale, condividendole opzionalmente su asciiname.org."
content_hash: 0f787e09eca8587e36b702f0ec9e56ffd5140421
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
  - title: 한국어 version
    url: /ko/common/asciinema.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/asciinema.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/asciinema.html
    icon: bi bi-globe
---
# asciinema

Registra e riproduci sessioni di terminale, condividendole opzionalmente su asciiname.org.
Maggiori informazioni: <https://asciinema.org/>.

- Associa l'installazione locale di `asciiname` ad un account di asciiname.org:

`asciinema auth`

- Avvia una nuova registrazione (una volta terminata, verrà chiesto se caricarla o salvarla localmente):

`asciinema rec`

- Avvia una nuova registrazione e salvala come file locale:

`asciinema rec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_registrazione</span>`.cast`

- Riproduci una sessione da un file locale:

`asciinema play `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file</span>`.cast`

- Riproducei una sessione da asciinema.org:

`asciinema play https://asciinema.org/a/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_registrazione</span>

- Avvia una nuova registrazione, limitando qualsiasi periodo di inattività a 2.5 secondi:

`asciinema rec -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2.5</span>

- Stampa l'output completo di una sessione locale:

`asciinema cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file</span>`.cast`

- Carica una sessione locale su asciinama.org:

`asciinema upload `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file</span>`.cast`

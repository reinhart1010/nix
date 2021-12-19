---
layout: page
title: common/electrum (italiano)
description: "Ergonomico wallet (portafogli) Bitcoin e gestore di chiavi private."
content_hash: 9f78440684a542025e5c43863518fd3f3ea2feb4
related_topics:
  - title: English version
    url: /en/common/electrum.html
    icon: bi bi-globe
---
# electrum

Ergonomico wallet (portafogli) Bitcoin e gestore di chiavi private.
Maggiori informazioni: <https://electrum.org>.

- Crea un nuovo wallet:

`electrum -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nuovo_wallet.dat</span>` create`

- Ripristina un wallet esistente da un seed offline:

`electrum -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wallet_ripristinato.dat</span>` restore -o`

- Crea una transazione firmata offline:

`electrum mktx `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">destinatario</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ammontare</span>` -f 0.0000001 -F `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mittente</span>` -o`

- Mostra tutti gli indirizzi del wallet per la ricezione:

`electrum listaddresses -a`

- Firma un messaggio:

`electrum signmessage `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">indirizzo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">messaggio</span>

- Verifica un messaggio:

`electrum verifymessage `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">indirizzo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">firma</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">messaggio</span>

- Connettiti solo ad una specifica istanza electrum-server:

`electrum -p socks5:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">127.0.0.1</span>`:9050 -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">56ckl5obj37gypcu.onion</span>`:50001:t -1`

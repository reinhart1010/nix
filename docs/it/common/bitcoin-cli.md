---
layout: page
title: common/bitcoin-cli (italiano)
description: "Client da linea di comando per interagire con il demone Bitcoin tramite chiamate RPC."
content_hash: d5271b0f56bed41cbad4742f52617b010168d3c7
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/bitcoin-cli.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/bitcoin-cli.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/bitcoin-cli.html
    icon: bi bi-globe
tldri18n_status: 2
---
# bitcoin-cli

Client da linea di comando per interagire con il demone Bitcoin tramite chiamate RPC.
Utilizza la configurazione definita in `bitcoin.conf`.
Maggiori informazioni: <https://en.bitcoin.it/wiki/Running_Bitcoin#Command-line_arguments>.

- Invia una transazione ad un dato indirizzo:

`bitcoin-cli sendtoaddress "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">indirizzo</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">importo</span>

- Genera uno o più blocchi:

`bitcoin-cli generate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">numero_blocchi</span>

- Mostra informazioni di alto livello sul portafogli:

`bitcoin-cli getwalletinfo`

- Elenca tutti gli output di transazioni precedenti disponibili per finanziare una nuove transazioni:

`bitcoin-cli listunspent`

- Esporta le informazioni sul portafogli in un file di testo:

`bitcoin-cli dumpwallet "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file</span>`"`

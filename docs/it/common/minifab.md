---
layout: page
title: common/minifab (italiano)
description: "Strumento per semplificare il settaggio e il deployment di una blockchain Hyperledger Fabric."
content_hash: 1feea836763907c356cd9b786c105b09334a7b29
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/minifab.html
    icon: bi bi-globe
tldri18n_status: 2
---
# minifab

Strumento per semplificare il settaggio e il deployment di una blockchain Hyperledger Fabric.
Maggiori informazioni: <https://github.com/hyperledger-labs/minifabric>.

- Crea la blockchain Hyperledger Fabric:

`minifab up -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">versione_minifab</span>

- Rimuovi la blockchain Hyperledger Fabric:

`minifab down`

- Installa smart contract su un canale:

`minifab install -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_smart_contract</span>

- Installa smart contract su un canale specificando la versione:

`minifab install -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_smart_contract</span>` -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">versione_smart_contract</span>

- Inizializza smart contract dopo installazione/aggiornamento dello stesso:

`minifab approve,commit,initialize,discover`

- Interroga smart contract con argomenti:

`minifab invoke -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_smart_contract</span>` -p '"`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_metodo</span>`", "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arg0</span>`", "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arg1</span>`", ...'`

- Interroga la blockchain:

`minifab blockquery `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">numero_blocco</span>

- Esegui direttamente l'applicazione:

`minifab apprun -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">linguaggio_di_programmazione</span>

---
layout: page
title: common/cabal (italiano)
description: "Interfaccia da linea di comando per l'infrastruttura di compilazione di Haskell (Cabal)."
content_hash: a0d4565a69cef55e5c65ecdb22c0e3ee59ea40b0
last_modified_at: 2024-05-23
related_topics:
  - title: English version
    url: /en/common/cabal.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/cabal.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/cabal.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/cabal.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cabal

Interfaccia da linea di comando per l'infrastruttura di compilazione di Haskell (Cabal).
Gestisce progetti Haskell e pacchetti Cabal dal repository di pacchetti Hackage.
Maggiori informazioni: <https://cabal.readthedocs.io/en/latest/getting-started.html>.

- Cerca ed elenca pacchetti da Hackage:

`cabal list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">termine_di_ricerca</span>

- Mostra informazioni su di un pacchetto:

`cabal info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_pacchetto</span>

- Scarica ed installa un pacchetto:

`cabal install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_pacchetto</span>

- Crea un nuovo progetto Haskell nella directory corrente:

`cabal init`

- Compila il progetto nella directory corrente:

`cabal build`

- Esegui i test del progetto nella directory corrente:

`cabal test`

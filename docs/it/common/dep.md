---
layout: page
title: common/dep (italiano)
description: "Strumento di gestione delle dipendenze per progetti Go."
content_hash: b5c06761af3182d43300bbd39cdfa3a736d64558
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/dep.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/dep.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># dep

Strumento di gestione delle dipendenze per progetti Go.
Maggiori informazioni: <https://deployer.org>.

- Inizializza la directory corrente come radice di un progetto Go:

`dep init`

- Installa dipendenze mancanti (scannerizza `Gopkg.toml` ed i file `.go`):

`dep ensure`

- Mostra lo stato delle dipendenze di un progetto:

`dep status`

- Aggiungi una dipendenza al progetto:

`dep ensure -add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url_pacchetto</span>

- Aggiorna le versioni bloccate (in `Gopkg.lock`) di tutte le dipendenze:

`dep ensure -update`

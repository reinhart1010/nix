---
layout: page
title: common/behat (italiano)
description: "Un framework PHP per lo sviluppo quidato dal comportamento."
content_hash: f7eedb2f95a7079e6b3d0a95fa8e2dcc838af24e
last_modified_at: 2024-10-13
related_topics:
  - title: English version
    url: /en/common/behat.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/behat.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/behat.html
    icon: bi bi-globe
tldri18n_status: 2
---
# behat

Un framework PHP per lo sviluppo quidato dal comportamento.
Maggiori informazioni: <https://behat.org>.

- Inizializza un nuovo progetto Behat:

`behat --init`

- Esegui tutti i test:

`behat`

- Esegui tutti i test di una specifica suite:

`behat --suite `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_suite</span>

- Esegui i test con uno specifico formato di output:

`behat --format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pretty|progress</span>

- Esegui i testi e scrivi i risultati in un file:

`behat --out `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file</span>

- Mostra una lista delle definizioni nelle suite di test:

`behat --definitions`

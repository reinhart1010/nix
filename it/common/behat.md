---
layout: page
title: common/behat (italiano)
description: "Un framework PHP per lo sviluppo quidato dal comportamento."
content_hash: 77389746775d25d1ee6172c20add2f61ce254587
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
---
# behat

Un framework PHP per lo sviluppo quidato dal comportamento.
Maggiori informazioni: <https://behat.org>.

- Inizializza un nuovo progetto Behat:

`behat --init`

- Esegui tutti i test:

`behat`

- Esegui tutti i test di una specifica suite:

`behat --suite=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_suite</span>

- Esegui i test con uno specifico formato di output:

`behat --format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pretty|progress</span>

- Esegui i testi e scrivi i risultati in un file:

`behat --out `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/a/file</span>

- Mostra una lista delle definizioni nelle suite di test:

`behat --definitions`

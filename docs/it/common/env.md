---
layout: page
title: common/env (italiano)
description: "Mostra le variabili d'ambiente o esegui un programma in un ambiente modificato."
content_hash: 0cf7ff06410417ad6757f02af0e5bd2635a6883e
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/env.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/env.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/env.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/env.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/env.html
    icon: bi bi-globe
  - title: norsk version
    url: /no/common/env.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># env

Mostra le variabili d'ambiente o esegui un programma in un ambiente modificato.
Maggiori informazioni: <https://www.gnu.org/software/coreutils/manual/html_node/env-invocation.html>.

- Mostra le variabili d'ambiente:

`env`

- Esegui un programma. Utilizzato spesso in script dopo lo shebang (#!) per cercare il percorso del programma:

`env `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">programma</span>

- Resetta l'ambiente ed esegui un programma:

`env -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">programma</span>

- Rimuovi una variabile dall'ambiente ed esegui un programma:

`env -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variabile</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">programma</span>

- Setta una variabile ed esegui un programma:

`env `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variabile</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">valore</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">programma</span>

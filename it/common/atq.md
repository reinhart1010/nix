---
layout: page
title: common/atq (italiano)
description: "Mostra job programmati dai comandi `at` o `batch`."
content_hash: 3d3e39d781ebf25f4e16e57f90c7bab823178289
related_topics:
  - title: English version
    url: /en/common/atq.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/atq.html
    icon: bi bi-globe
---
# atq

Mostra job programmati dai comandi `at` o `batch`.
Maggiori informazioni: <https://manned.org/atq>.

- Mostra i job programmati per l'utente corrente:

`atq`

- Mostra i job della coda 'a' (le code hanno nomi di un singolo carattere):

`atq -q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">a</span>

- Mostra i job di tutti gli utenti (da eseguire come super user):

`sudo atq`

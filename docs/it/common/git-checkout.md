---
layout: page
title: common/git-checkout (italiano)
description: "Cambia rami o ripristina i file dell'albero di lavoro."
content_hash: 54062c91d5ce09cf62ffda1130289e061551b51d
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/git-checkout.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-checkout.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-checkout.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/git-checkout.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git-checkout.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-checkout.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-checkout.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/git-checkout.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># git checkout

Cambia rami o ripristina i file dell'albero di lavoro.
Maggiori informazioni: <https://git-scm.com/docs/git-checkout>.

- Crea e passa ad un nuovo ramo:

`git checkout -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_ramo</span>

- Crea e passa ad un nuovo ramo a partire dal riferimento specificato (ramo-locale, remote/ramo-remoto, tag sono alcuni esempi di riferimenti validi):

`git checkout -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_ramo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">riferimento</span>

- Passa ad un ramo locale esistente:

`git checkout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_ramo</span>

- Passa ad un ramo remoto esistente:

`git checkout --track `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_repository_remoto</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_ramo</span>

- Annulla tutte le modifiche nella directory corrente che non sono state aggiunte all'area di stage (vedi `git reset` per più comandi simili):

`git checkout .`

- Annulla tutte le modifiche di un dato file non aggiunte all'area di stage:

`git checkout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_file</span>

- Sostituisci un file con il contenuto del suo corrispondente localizzato su un altro ramo:

`git checkout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_ramo</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_file</span>

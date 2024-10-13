---
layout: page
title: common/git-branch (italiano)
description: "Il principale comando Git per lavorare con i rami."
content_hash: 179259d36f7caf29e3cc8d69fd7b4b9393926f0c
last_modified_at: 2024-10-13
related_topics:
  - title: Deutsch version
    url: /de/common/git-branch.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-branch.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-branch.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-branch.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/git-branch.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/git-branch.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git-branch.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-branch.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-branch.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># git branch

Il principale comando Git per lavorare con i rami.
Maggiori informazioni: <https://git-scm.com/docs/git-branch>.

- Elenca i rami locali. Il ramo corrente è evidenziato da un `*`:

`git branch`

- Elenca tutti i rami (locali e remoti):

`git branch -a`

- Crea un nuovo ramo a partire dal commit corrente:

`git branch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_ramo</span>

- Crea un nuovo ramo a partire dal commit specificato:

`git branch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_ramo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hash_commit</span>

- Rinomina un ramo (non applicabile sul ramo corrente):

`git branch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-m|--move</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vecchio_nome</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nuovo_nome</span>

- Cancella un ramo locale (non applicabile sul ramo corrente):

`git branch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-d|--delete</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_ramo</span>

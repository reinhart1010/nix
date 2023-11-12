---
layout: page
title: common/git-commit (italiano)
description: "Salva file nell'area di stage in una nuova istantanea del tuo repository."
content_hash: 98ce43f11d249f84f39b62e76234c4c8f388e6fb
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/git-commit.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-commit.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-commit.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-commit.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/git-commit.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/git-commit.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git-commit.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-commit.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-commit.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/git-commit.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># git commit

Salva file nell'area di stage in una nuova istantanea del tuo repository.
Maggiori informazioni: <https://git-scm.com/docs/git-commit>.

- Committa sul repository i file nell'area di stage con un messaggio:

`git commit -m "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">messaggio</span>`"`

- Aggiungi all'area di stage tutti i file modificati e committali con un messaggio:

`git commit -a -m "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">messaggio</span>`"`

- Sostituisci l'ultimo commit con le modifiche attualmente salvate nell'area di stage:

`git commit --amend`

- Committa solo i file specificati (tra quelli presenti nell'area di stage):

`git commit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file2</span>

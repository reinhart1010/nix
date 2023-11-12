---
layout: page
title: common/git-status (italiano)
description: "Mostra le modifiche ai file in un repository Git."
content_hash: bfcef2574e1c5564510087be2251c41069d536fd
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/git-status.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-status.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-status.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-status.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/git-status.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/git-status.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git-status.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-status.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/git-status.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># git status

Mostra le modifiche ai file in un repository Git.
Elenca i file modificati, aggiunti e cancellati rispetto al commit corrente.
Maggiori informazioni: <https://git-scm.com/docs/git-status>.

- Mostra i file modificati che non sono stati ancora committati:

`git status`

- Mostra l'output in formato ridotto:

`git status -s`

- Nascondi i file non tracciati dall'output:

`git status --untracked-files=no`

- Mostra informazioni sul ramo ed in formato ridotto:

`git status -sb`

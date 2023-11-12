---
layout: page
title: common/git-add (italiano)
description: "Aggiungi file nuovi o modificati all'area di stage."
content_hash: 68f693efc99eeecb87e0366a53148cddc53474da
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/git-add.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-add.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-add.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-add.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/git-add.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/git-add.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git-add.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-add.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-add.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/git-add.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># git add

Aggiungi file nuovi o modificati all'area di stage.
Maggiori informazioni: <https://git-scm.com/docs/git-add>.

- Aggiungi un file all'area di stage:

`git add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file</span>

- Aggiungi tutti i file (tracciati e non tracciati):

`git add -A`

- Aggiungi solo i file già tracciati:

`git add -u`

- Aggiungi anche i file ignorati:

`git add -f`

- Aggiungi parti di un file in modo interattivo:

`git add -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file</span>

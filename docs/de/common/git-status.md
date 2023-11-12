---
layout: page
title: common/git-status (Deutsch)
description: "Zeige die Änderungen an Dateien in einem Git-Repository an."
content_hash: 11af5d1b49fa876b8b6692654b8eb50f4cc2c753
last_modified_at: 2023-11-12
related_topics:
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
  - title: italiano version
    url: /it/common/git-status.html
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

Zeige die Änderungen an Dateien in einem Git-Repository an.
Weitere Informationen: <https://git-scm.com/docs/git-status>.

- Zeige veränderte Dateien an, die noch nicht für den Commit hinzugefügt wurden:

`git status`

- Zeige eine kurze Version an:

`git status -s`

- Zeige nur verfolgte (getrackte) Dateien an:

`git status --untracked-files=no`

- Zeige eine kurze Version mit zusätzlichen Informationen über den Branch an:

`git status -sb`

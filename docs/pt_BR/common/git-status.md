---
layout: page
title: common/git-status (português (Brasil))
description: "Mostra as alterações nos arquivos em um repositório Git."
content_hash: fe79fbadbd35d593886ba85487e98b2bb5461c7a
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
  - title: italiano version
    url: /it/common/git-status.html
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

Mostra as alterações nos arquivos em um repositório Git.
Lista os arquivos alterados, adicionados e excluídos em comparação com o atual commit verificado.
Mais informações: <https://git-scm.com/docs/git-status>.

- Mostra arquivos alterados que ainda não foram adicionados para commit:

`git status`

- Fornece a saída em formato curto:

`git status -s`

- Não mostra arquivos não rastreados na saída:

`git status --untracked-files=no`

- Mostra a saída em formato curto junto com as informações da branch:

`git status -sb`

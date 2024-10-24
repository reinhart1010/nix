---
layout: page
title: common/git-status (português (Brasil))
description: "Mostra as alterações nos arquivos em um repositório Git."
content_hash: b8190f001efde9ea298a0bbddce6106b9fa01f3b
last_modified_at: 2024-10-24
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
  - title: 한국어 version
    url: /ko/common/git-status.html
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
Lista os arquivos alterados, adicionados e excluídos em comparação com o atual commit do checkout.
Mais informações: <https://git-scm.com/docs/git-status>.

- Mostra arquivos alterados que ainda não foram adicionados para commit:

`git status`

- Fornece a saída em formato curto:

`git status --short`

- Mostra informação verbosa em alterações tanto na área de preparação e no diretório de trabalho:

`git status --verbose --verbose`

- Mostra informações da branch e de rastreamento:

`git status --branch`

- Mostra a saída em formato curto junto com as informações da branch:

`git status --short --branch`

- Mostra o número de entradas atualmente armazenadas:

`git status --show-stash`

- Não mostra arquivos não rastreados na saída:

`git status --untracked-files=no`

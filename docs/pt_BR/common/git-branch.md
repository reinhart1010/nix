---
layout: page
title: common/git-branch (português (Brasil))
description: "Comando principal do Git para trabalhar com branches."
content_hash: d7eb2213546cf3a5a508d1b9eb328ba7df9c5f44
last_modified_at: 2023-10-15
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
  - title: italiano version
    url: /it/common/git-branch.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-branch.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-branch.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># git branch

Comando principal do Git para trabalhar com branches.
Mais informações: <https://git-scm.com/docs/git-branch>.

- Lista todas as branches (locais e remotas; a branch atual é destacada por `*`):

`git branch --all`

- Lista quais branches incluem um commit específico do Git em seu histórico:

`git branch --all --contains `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hash_do_commit</span>

- Mostra o nome da branch atual:

`git branch --show-current`

- Cria uma nova branch baseada no commit atual:

`git branch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_da_branch</span>

- Crua uma nova branch baseada em um commit específico:

`git branch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_da_branch</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hash_do_commit</span>

- Renomeia uma branch (não precisa fazer checkout para isso):

`git branch -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">antigo_nome_da_branch</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">novo_nome_da_branch</span>

- Exclui a branch local (não precisa fazer checkout para isso):

`git branch -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_da_branch</span>

- Exclui uma branch remota:

`git push `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_remoto</span>` --delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_da_branch_remota</span>

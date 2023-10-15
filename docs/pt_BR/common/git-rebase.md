---
layout: page
title: common/git-rebase (português (Brasil))
description: "Reaplica os commits de uma branch sobre outra branch."
content_hash: a94e247f6b89d02553066498487428df37cc1528
last_modified_at: 2023-10-15
related_topics:
  - title: Deutsch version
    url: /de/common/git-rebase.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-rebase.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-rebase.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-rebase.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-rebase.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-rebase.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/git-rebase.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># git rebase

Reaplica os commits de uma branch sobre outra branch.
Comumente usado para "mover" uma branch inteira para outra base, criando cópias dos commits na nova localização.
Mais informações: <https://git-scm.com/docs/git-rebase>.

- Faz um rebase na branch atual sobre outra branch especificada:

`git rebase `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nova_branch_base</span>

- Inicia um rebase interativo, que permite os commits serem reordenados, omitidos, combinados ou modificados:

`git rebase -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch_base_alvo_ou_hash_do_commit</span>

- Continua um rebase que foi interrompido por uma falha de mesclagem, após a edição de arquivos conflitantes:

`git rebase --continue`

- Continua um rebase que foi pausado devido a conflitos de mesclagem, ignorando o commit conflitante:

`git rebase --skip`

- Aborta um rebase em andamento (por exemplo, se ele foi interrompido por um conflito de mesclagem):

`git rebase --abort`

- Move parte da branch atual para uma nova base, fornecendo a base antiga para começar:

`git rebase --onto `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">base_nova</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">base_antiga</span>

- Reaplica os últimos 5 commits no local, parando para permitir que eles sejam reordenados, omitidos, combinados ou modificados:

`git rebase -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HEAD~5</span>

- Resolve automaticamente quaisquer conflitos favorecendo a versão da branch de trabalho (a palavra-chave `theirs` tem significado invertido nesse caso):

`git rebase -X theirs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_da_branch</span>

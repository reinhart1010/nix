---
layout: page
title: common/git-diff (português (Brasil))
description: "Mostra alterações nos arquivos rastreados."
content_hash: 1519e2cbdd77ee69e3fb518accd04c3dd300ef24
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/git-diff.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-diff.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-diff.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-diff.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-diff.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git diff

Mostra alterações nos arquivos rastreados.
Mais informações: <https://git-scm.com/docs/git-diff>.

- Mostra as alterações não preparadas e sem commit:

`git diff`

- Mostra todas as alterações sem commit (incluindo as preparadas):

`git diff HEAD`

- Mostra apenas as alterações preparadas (adicionadas, mas ainda sem commit):

`git diff --staged`

- Mostra as alterações de todos os commits desde uma determinada data/hora (uma expressão de data, por exemplo, "1 week 2 days" ou uma data ISO):

`git diff 'HEAD@{3 months|weeks|days|hours|seconds ago}'`

- Mostra apenas os nomes dos arquivos alterados desde um determinado commit:

`git diff --name-only `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>

- Emite um resumo das criações de arquivos, renomeações e alterações de modo desde um determinado commit:

`git diff --summary `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>

- Compara um único arquivo entre duas branches ou commits:

`git diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch_1</span>`..`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch_2</span>` [--] `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>

- Compara diferentes arquivos da branch atual com outra branch:

`git diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>

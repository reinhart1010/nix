---
layout: page
title: common/git-checkout (português (Brasil))
description: "Faz checkout de uma branch ou caminhos para uma árvore de trabalho."
content_hash: 1cb6b52c815cb90392ba188beb89ae7da551d0c9
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/git-checkout.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-checkout.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-checkout.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/git-checkout.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-checkout.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-checkout.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-checkout.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/git-checkout.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git checkout

Faz checkout de uma branch ou caminhos para uma árvore de trabalho.
Mais informações: <https://git-scm.com/docs/git-checkout>.

- Cria e muda para uma nova branch:

`git checkout -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_da_branch</span>

- Cria e muda para uma nova branch com base em uma referência específica (branch, remoto/branch, etiqueta são exemplos de referências válidas):

`git checkout -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_da_branch</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">referência</span>

- Muda para uma branch local existente:

`git checkout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_da_branch</span>

- Muda para uma branch previamente verificada:

`git checkout -`

- Muda para uma branch remota existente:

`git checkout --track `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_remoto</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_da_branch</span>

- Descarta todas as alterações não preparadas no diretório atual (consulte `git reset` para mais comandos do tipo desfazer):

`git checkout .`

- Descarta alterações não preparadas em um determinado arquivo:

`git checkout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>

- Substitui um arquivo no diretório atual com a versão com commit em uma determinada branch:

`git checkout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_da_branch</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>

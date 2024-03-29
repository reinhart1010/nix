---
layout: page
title: common/git-reset (português (Brasil))
description: "Desfaz os commits ou as alterações nào preparadas, redefinindo o Git HEAD atual para o estado especificado."
content_hash: 68b9a525eaa1a962e1afccfb10b9527f268a93cf
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/git-reset.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-reset.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-reset.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-reset.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-reset.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git reset

Desfaz os commits ou as alterações nào preparadas, redefinindo o Git HEAD atual para o estado especificado.
Se um caminho é passado, funcionará como "não preparado"; se um hash de commit ou uma branch é passado, funcionará como "sem commit".
Mais informações: <https://git-scm.com/docs/git-reset>.

- Remove tudo da preparação:

`git reset`

- Remove arquivo(s) específico(s) da preparação:

`git reset `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo1 caminho/para/arquivo2 ...</span>

- Interativamente remove partes de um arquivo da preparação:

`git reset --patch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>

- Desfaz o último commit, mantendo suas alterações (e quaisquer outras alteração não confirmadas) no sistema de arquivos:

`git reset HEAD~`

- Desfaz os últimos dois commits, adicionando suas alterações na área de preparação, isso é, preparando-os para o commit:

`git reset --soft HEAD~2`

- Descarta quaisquer alterações sem commit, preparadas ou não (para apenas alterações não preparadas, use o `git checkout`):

`git reset --hard`

- Redefine o repositório para um determinado commit, descartando as alterações com commit, preparadas e sem commit desde então:

`git reset --hard `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>

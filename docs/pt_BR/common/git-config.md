---
layout: page
title: common/git-config (português (Brasil))
description: "Gerencia configurações customizadadas para repositórios Git."
content_hash: c716dee6159c278794719e0cb846470ae7285228
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/git-config.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-config.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-config.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-config.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-config.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-config.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/git-config.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/git-config.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git config

Gerencia configurações customizadadas para repositórios Git.
Estas configurações podem ser locais (para o repositório corrente) ou globais (para o usuário atual).
Mais informações: <https://git-scm.com/docs/git-config>.

- Lista somente configurações locais (armazenadas no `.git/config` do repositório corrente):

`git config --list --local`

- Lista somente configurações globais (armazenadas no `~/.gitconfig` por padrão ou no `$XDG_CONFIG_HOME/git/config` se tal arquivo existe):

`git config --list --global`

- Lista somente configurações do sistema (armazenadas no `/etc/gitconfig`), e exibe o local do arquivo:

`git config --list --system --show-origin`

- Obtém o valor de uma dada variável de configuração:

`git config alias.unstage`

- Armazena o valor global de uma dada variável de configuração:

`git config --global alias.unstage "reset HEAD --"`

- Reverte o valor global de uma dada variável de configuração para seu valor padrão:

`git config --global --unset alias.unstage`

- Edita a configuração Git do repositório corrente usando o editor padrão:

`git config --edit`

- Edita a configuração global do Git usando o editor padrão:

`git config --global --edit`

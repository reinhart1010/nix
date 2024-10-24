---
layout: page
title: common/git-config (português (Brasil))
description: "Gerencia configurações personalizadas para repositórios Git."
content_hash: 57e440c4f0a295b06ebb16077c23581767c39e89
last_modified_at: 2024-10-24
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
  - title: Indonesia version
    url: /id/common/git-config.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-config.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/git-config.html
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

Gerencia configurações personalizadas para repositórios Git.
Estas configurações podem ser locais (para o repositório atual) ou globais (para o usuário atual).
Mais informações: <https://git-scm.com/docs/git-config>.

- Define globalmente seu nome ou e-mail (essas informações são necessárias para fazer commit em um repositório e serão incluídas em todos os commits):

`git config --global `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user.name|user.email</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Seu nome|e-mail@example.com</span>`"`

- Lista configurações locais ou globais:

`git config --list --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">local|global</span>

- Lista somente configurações do sistema (armazenadas no `/etc/gitconfig`), e exibe o local do arquivo:

`git config --list --system --show-origin`

- Obtém o valor de uma dada configuração:

`git config alias.unstage`

- Define o valor global de uma dada configuração:

`git config --global alias.unstage "reset HEAD --"`

- Reverte a configuração global para seu valor padrão:

`git config --global --unset alias.unstage`

- Edita a configuração local do Git (`.git/config`) no editor padrão:

`git config --edit`

- Edita a configuração global do Git (`~/.gitconfig` por padrão ou `$XDG_CONFIG_HOME/git/config` se tal arquivo existir) no editor padrão:

`git config --global --edit`

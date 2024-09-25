---
layout: page
title: common/docker-login (português (Brasil))
description: "Fazer login em um registro do Docker."
content_hash: 15f66eff3c8229f5b5e609306546e26d210b6562
last_modified_at: 2024-09-25
related_topics:
  - title: Deutsch version
    url: /de/common/docker-login.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-login.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-login.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker login

Fazer login em um registro do Docker.
Mais informações: <https://docs.docker.com/reference/cli/docker/login/>.

- Faz login interativamente em um registro:

`docker login`

- Faz login em um registro com um nome de usuário específico (será solicitada a senha):

`docker login --username `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_de_usuário</span>

- Faz login em um registro com nome de usuário e senha:

`docker login --username `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_de_usuário</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">senha</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">servidor</span>

- Faz login em um registro com a senha vinda do `stdin`:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">senha</span>`" | docker login --username `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_de_usuário</span>` --password-stdin`

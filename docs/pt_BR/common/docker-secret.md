---
layout: page
title: common/docker-secret (português (Brasil))
description: "Gerenciar segredos do Docker swarm."
content_hash: d79d564ff414e0bf52ef3eab07f22160af84b34f
last_modified_at: 2024-09-26
related_topics:
  - title: Deutsch version
    url: /de/common/docker-secret.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-secret.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-secret.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker-secret.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker secret

Gerenciar segredos do Docker swarm.
Mais informações: <https://docs.docker.com/reference/cli/docker/secret/>.

- Cria um novo segredo a partir de `stdin`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>` | docker secret create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_segredo</span>` -`

- Cria um novo segredo a partir de um arquivo:

`docker secret create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_segredo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>

- Lista todos os segredos:

`docker secret ls`

- Exibe informações detalhadas sobre um ou vários segredos em um formato amigável ao usuário:

`docker secret inspect --pretty `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_segredo1 nome_do_segredo2 ...</span>

- Remove um ou mais segredos:

`docker secret rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_segredo1 nome_do_segredo2 ...</span>

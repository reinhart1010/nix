---
layout: page
title: common/docker-secret (português (Brasil))
description: "Gerenciar segredos do Docker swarm."
content_hash: 0ec7753a478e036855f0b64e50cceb1ddc84d11a
last_modified_at: 2023-09-20
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
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># docker secret

Gerenciar segredos do Docker swarm.
Mais informações: <https://docs.docker.com/engine/reference/commandline/secret/>.

- Criar um novo segredo a partir de `stdin`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>` | docker secret create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_segredo</span>` -`

- Criar um novo segredo a partir de um arquivo:

`docker secret create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_segredo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>

- Listar todos os segredos:

`docker secret ls`

- Exibir informações detalhadas sobre um ou vários segredos em um formato amigável ao usuário:

`docker secret inspect --pretty `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_segredo1 nome_do_segredo2 ...</span>

- Remover um ou mais segredos:

`docker secret rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_segredo1 nome_do_segredo2 ...</span>

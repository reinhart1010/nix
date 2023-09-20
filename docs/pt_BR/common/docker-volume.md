---
layout: page
title: common/docker-volume (português (Brasil))
description: "Gerenciar volumes do Docker."
content_hash: 9d06f4181d89fe7af0078e5c0af098a1fc48d493
last_modified_at: 2023-09-20
related_topics:
  - title: English version
    url: /en/common/docker-volume.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-volume.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># docker volume

Gerenciar volumes do Docker.
Mais informações: <https://docs.docker.com/engine/reference/commandline/volume/>.

- Criar um volume:

`docker volume create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_volume</span>

- Criar um volume com um rótulo específico:

`docker volume create --label `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rótulo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_volume</span>

- Criar um volume `tmpfs` com tamanho de 100 MiB e uid 1000:

`docker volume create --opt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">type</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tmpfs</span>` --opt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">device</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tmpfs</span>` --opt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">o</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">size=100m,uid=1000</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_volume</span>

- Listar todos os volumes:

`docker volume ls`

- Remover um volume:

`docker volume rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_volume</span>

- Exibir informações sobre um volume:

`docker volume inspect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_volume</span>

- Remover todos os volumes locais não utilizados:

`docker volume prune`

- Exibir ajuda para um subcomando:

`docker volume `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subcomando</span>` --help`

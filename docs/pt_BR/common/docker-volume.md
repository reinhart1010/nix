---
layout: page
title: common/docker-volume (português (Brasil))
description: "Gerenciar volumes do Docker."
content_hash: bd01de217892ce3826b7b0994fc19797843bc86e
last_modified_at: 2023-12-28
related_topics:
  - title: English version
    url: /en/common/docker-volume.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-volume.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker volume

Gerenciar volumes do Docker.
Mais informações: <https://docs.docker.com/engine/reference/commandline/volume/>.

- Cria um volume:

`docker volume create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_volume</span>

- Cria um volume com um rótulo específico:

`docker volume create --label `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rótulo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_volume</span>

- Cria um volume `tmpfs` com tamanho de 100 MiB e uid 1000:

`docker volume create --opt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">type</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tmpfs</span>` --opt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">device</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tmpfs</span>` --opt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">o</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">size=100m,uid=1000</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_volume</span>

- Lista todos os volumes:

`docker volume ls`

- Remove um volume:

`docker volume rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_volume</span>

- Exibe informações sobre um volume:

`docker volume inspect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_volume</span>

- Remove todos os volumes locais não utilizados:

`docker volume prune`

- Exibe ajuda para um subcomando:

`docker volume `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subcomando</span>` --help`

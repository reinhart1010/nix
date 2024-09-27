---
layout: page
title: common/docker-pull (português (Brasil))
description: "Baixar imagens do Docker de um registro."
content_hash: 9382e9c88abdc1b8653d0c9651ff012022b65dba
last_modified_at: 2024-09-27
related_topics:
  - title: English version
    url: /en/common/docker-pull.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-pull.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker pull

Baixar imagens do Docker de um registro.
Mais informações: <https://docs.docker.com/reference/cli/docker/image/pull/>.

- Baixa uma imagem específica do Docker:

`docker pull `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imagem</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag</span>

- Baixa uma imagem específica do Docker no modo silencioso:

`docker pull --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imagem</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag</span>

- Baixa todas as tags de uma imagem específica do Docker:

`docker pull --all-tags `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imagem</span>

- Baixa imagens do Docker para uma plataforma específica, por exemplo, linux/amd64:

`docker pull --platform `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">linux/amd64</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imagem</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag</span>

- Exibe ajuda:

`docker pull --help`

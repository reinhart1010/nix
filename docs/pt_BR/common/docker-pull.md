---
layout: page
title: common/docker-pull (português (Brasil))
description: "Baixar imagens do Docker de um registro."
content_hash: 2d77ba2432d28951b17641259a408e6beac6cc03
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/docker-pull.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker pull

Baixar imagens do Docker de um registro.
Mais informações: <https://docs.docker.com/engine/reference/commandline/pull/>.

- Baixar uma imagem específica do Docker:

`docker pull `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imagem</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag</span>

- Baixar uma imagem específica do Docker no modo silencioso:

`docker pull --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imagem</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag</span>

- Baixar todas as tags de uma imagem específica do Docker:

`docker pull --all-tags `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imagem</span>

- Baixar imagens do Docker para uma plataforma específica, por exemplo, linux/amd64:

`docker pull --platform `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">linux/amd64</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imagem</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag</span>

- Exibir ajuda:

`docker pull --help`

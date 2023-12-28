---
layout: page
title: common/docker-tag (português (Brasil))
description: "Atribuir tags a imagens Docker existentes."
content_hash: bedcc6fffa6ef5b730859a7755bfc233389e0e9f
last_modified_at: 2023-12-28
related_topics:
  - title: English version
    url: /en/common/docker-tag.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker tag

Atribuir tags a imagens Docker existentes.
Mais informações: <https://docs.docker.com/engine/reference/commandline/tag/>.

- Atribui um nome e tag a um ID de imagem específico:

`docker tag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag</span>

- Atribui uma tag a uma imagem específica:

`docker tag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imagem</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag_atual</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imagem</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nova_tag</span>

- Exibe ajuda:

`docker tag`

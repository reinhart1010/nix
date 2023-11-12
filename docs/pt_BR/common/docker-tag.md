---
layout: page
title: common/docker-tag (português (Brasil))
description: "Atribuir tags a imagens Docker existentes."
content_hash: 4b13e6d4e05f81bbdc9149d8a8cbf51807bfe6fe
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/docker-tag.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker tag

Atribuir tags a imagens Docker existentes.
Mais informações: <https://docs.docker.com/engine/reference/commandline/tag/>.

- Atribuir um nome e tag a um ID de imagem específico:

`docker tag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag</span>

- Atribuir uma tag a uma imagem específica:

`docker tag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imagem</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag_atual</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imagem</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nova_tag</span>

- Exibir ajuda:

`docker tag`

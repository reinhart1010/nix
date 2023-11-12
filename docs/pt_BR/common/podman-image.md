---
layout: page
title: common/podman-image (português (Brasil))
description: "Gerenciar imagens Docker."
content_hash: 30a79b11f7eb87e8c2c1c29170307a107a64e8b6
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/podman-image.html
    icon: bi bi-globe
tldri18n_status: 2
---
# podman image

Gerenciar imagens Docker.
Veja também `podman build`, `podman import` e `podman pull`.
Mais informações: <https://docs.podman.io/en/latest/markdown/podman-image.1.html>.

- Listar imagens Docker locais:

`podman image ls`

- Excluir imagens Docker locais não utilizadas:

`podman image prune`

- Excluir todas as imagens não utilizadas (não apenas aquelas sem uma tag):

`podman image prune --all`

- Mostrar o histórico de uma imagem Docker local:

`podman image history `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imagem</span>

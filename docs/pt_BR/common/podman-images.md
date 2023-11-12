---
layout: page
title: common/podman-images (português (Brasil))
description: "Gerenciar imagens do Podman."
content_hash: 3c1ed2fc664f5b87c1dd4e148b11f0baddf93fa7
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/podman-images.html
    icon: bi bi-globe
tldri18n_status: 2
---
# podman images

Gerenciar imagens do Podman.
Mais informações: <https://docs.podman.io/en/latest/markdown/podman-images.1.html>.

- Listar todas as imagens do Podman:

`podman images`

- Listar todas as imagens do Podman, incluindo intermediárias:

`podman images --all`

- Listar a saída no modo silencioso (apenas IDs numéricos):

`podman images --quiet`

- Listar todas as imagens do Podman que não são utilizadas por nenhum contêiner:

`podman images --filter dangling=true`

- Listar imagens que contenham uma substring em seus nomes:

`podman images "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*imagem|imagem*</span>`"`

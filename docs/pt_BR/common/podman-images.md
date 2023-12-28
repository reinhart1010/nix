---
layout: page
title: common/podman-images (português (Brasil))
description: "Gerenciar imagens do Podman."
content_hash: dffc60269926252d8660ac9f92833da89afb27e2
last_modified_at: 2023-12-28
related_topics:
  - title: English version
    url: /en/common/podman-images.html
    icon: bi bi-globe
tldri18n_status: 2
---
# podman images

Gerenciar imagens do Podman.
Mais informações: <https://docs.podman.io/en/latest/markdown/podman-images.1.html>.

- Lista todas as imagens do Podman:

`podman images`

- Lista todas as imagens do Podman, incluindo intermediárias:

`podman images --all`

- Lista a saída no modo silencioso (apenas IDs numéricos):

`podman images --quiet`

- Lista todas as imagens do Podman que não são utilizadas por nenhum contêiner:

`podman images --filter dangling=true`

- Lista imagens que contenham uma substring em seus nomes:

`podman images "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*imagem|imagem*</span>`"`

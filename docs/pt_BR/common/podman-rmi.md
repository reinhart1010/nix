---
layout: page
title: common/podman-rmi (português (Brasil))
description: "Remover uma ou mais imagens do Podman."
content_hash: 204ff427be33fd7b8680586aee88ac83b5038dcc
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/podman-rmi.html
    icon: bi bi-globe
tldri18n_status: 2
---
# podman rmi

Remover uma ou mais imagens do Podman.
Mais informações: <https://docs.podman.io/en/latest/markdown/podman-rmi.1.html>.

- Remover uma ou mais imagens pelo nome delas:

`podman rmi `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imagem:tag</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imagem2:tag</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">...</span>

- Remover uma imagem forçadamente:

`podman rmi --force `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imagem</span>

- Remover uma imagem sem excluir os pais não marcados:

`podman rmi --no-prune `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imagem</span>

- Exibir ajuda:

`podman rmi`

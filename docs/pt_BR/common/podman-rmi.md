---
layout: page
title: common/podman-rmi (português (Brasil))
description: "Remover uma ou mais imagens do Podman."
content_hash: 4dcdc4ce8f133f284073333ef93aeba7ce568d18
last_modified_at: 2023-12-28
related_topics:
  - title: English version
    url: /en/common/podman-rmi.html
    icon: bi bi-globe
tldri18n_status: 2
---
# podman rmi

Remover uma ou mais imagens do Podman.
Mais informações: <https://docs.podman.io/en/latest/markdown/podman-rmi.1.html>.

- Remove uma ou mais imagens pelo nome delas:

`podman rmi `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imagem:tag</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imagem2:tag</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">...</span>

- Remove uma imagem forçadamente:

`podman rmi --force `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imagem</span>

- Remove uma imagem sem excluir os pais não marcados:

`podman rmi --no-prune `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imagem</span>

- Exibe ajuda:

`podman rmi`

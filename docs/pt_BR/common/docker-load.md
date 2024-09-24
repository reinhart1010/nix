---
layout: page
title: common/docker-load (português (Brasil))
description: "Carregar imagens do Docker a partir de arquivos ou `stdin`."
content_hash: e332dc348b865f99d5b8c9a2077eb2aa390f8317
last_modified_at: 2024-09-24
related_topics:
  - title: English version
    url: /en/common/docker-load.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-load.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker load

Carregar imagens do Docker a partir de arquivos ou `stdin`.
Mais informações: <https://docs.docker.com/reference/cli/docker/image/load/>.

- Carrega uma imagem do Docker a partir do `stdin`:

`docker load < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_imagem.tar</span>

- Carrega uma imagem do Docker a partir de um arquivo específico:

`docker load --input `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_imagem.tar</span>

- Carrega uma imagem do Docker a partir de um arquivo específico no modo silencioso:

`docker load --quiet --input `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_imagem.tar</span>

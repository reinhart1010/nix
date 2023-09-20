---
layout: page
title: common/docker-load (português (Brasil))
description: "Carregar imagens do Docker a partir de arquivos ou `stdin`."
content_hash: 079699d3e500cf069fc8fa25ae73ab9fa02525e2
last_modified_at: 2023-09-20
related_topics:
  - title: English version
    url: /en/common/docker-load.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># docker load

Carregar imagens do Docker a partir de arquivos ou `stdin`.
Mais informações: <https://docs.docker.com/engine/reference/commandline/load/>.

- Carregar uma imagem do Docker a partir do `stdin`:

`docker load < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_imagem.tar</span>

- Carregar uma imagem do Docker a partir de um arquivo específico:

`docker load --input `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_imagem.tar</span>

- Carregar uma imagem do Docker a partir de um arquivo específico no modo silencioso:

`docker load --quiet --input `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_imagem.tar</span>

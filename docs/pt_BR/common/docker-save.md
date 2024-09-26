---
layout: page
title: common/docker-save (português (Brasil))
description: "Exportar uma ou mais imagens do Docker para um arquivo de arquivamento."
content_hash: 320d5a501fb3086adcf14321fc43f1e9b2f16527
last_modified_at: 2024-09-26
related_topics:
  - title: Deutsch version
    url: /de/common/docker-save.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-save.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-save.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker-save.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker save

Exportar uma ou mais imagens do Docker para um arquivo de arquivamento.
Mais informações: <https://docs.docker.com/reference/cli/docker/image/save/>.

- Salva uma imagem redirecionando `stdout` para um arquivo tar:

`docker save `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imagem</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.tar</span>

- Salva uma imagem em um arquivo tar:

`docker save --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.tar</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imagem</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag</span>

- Salva todas as tags da imagem:

`docker save --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.tar</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_da_imagem</span>

- Seleciona tags específicas de uma imagem para salvar:

`docker save --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.tar</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_da_imagem:tag1 nome_da_imagem:tag2 ...</span>

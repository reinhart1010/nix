---
layout: page
title: common/docker-save (português (Brasil))
description: "Exportar uma ou mais imagens do Docker para um arquivo de arquivamento."
content_hash: 769230305086eb8c278d236899dc14c002878c6c
last_modified_at: 2023-09-20
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
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># docker save

Exportar uma ou mais imagens do Docker para um arquivo de arquivamento.
Mais informações: <https://docs.docker.com/engine/reference/commandline/save/>.

- Salvar uma imagem redirecionando `stdout` para um arquivo tar:

`docker save `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imagem</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.tar</span>

- Salvar uma imagem em um arquivo tar:

`docker save --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.tar</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imagem</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag</span>

- Salvar todas as tags da imagem:

`docker save --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.tar</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_da_imagem</span>

- Selecionar tags específicas de uma imagem para salvar:

`docker save --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.tar</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_da_imagem:tag1 nome_da_imagem:tag2 ...</span>

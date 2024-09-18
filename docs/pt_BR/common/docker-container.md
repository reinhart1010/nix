---
layout: page
title: common/docker-container (português (Brasil))
description: "Gerenciar contêineres Docker."
content_hash: 6c978d7130c4e596cd38a8b75d3ce37f14838c3a
last_modified_at: 2024-09-18
related_topics:
  - title: Deutsch version
    url: /de/common/docker-container.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-container.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-container.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/docker-container.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/docker-container.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker container

Gerenciar contêineres Docker.
Mais informações: <https://docs.docker.com/reference/cli/docker/container/>.

- Lista os contêineres Docker em execução:

`docker container ls`

- Inicia um ou mais contêineres parados:

`docker container start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_contêiner1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_contêiner2</span>

- Encerra um ou mais contêineres em execução:

`docker container kill `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_contêiner</span>

- Para um ou mais contêineres em execução:

`docker container stop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_contêiner</span>

- Pausa todos os processos em um ou mais contêineres:

`docker container pause `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_contêiner</span>

- Exibe informações detalhadas sobre um ou mais contêineres:

`docker container inspect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_contêiner</span>

- Exporta o sistema de arquivos de um contêiner como um arquivo tar:

`docker container export `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_contêiner</span>

- Cria uma nova imagem a partir das alterações em um contêiner:

`docker container commit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_contêiner</span>

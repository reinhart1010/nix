---
layout: page
title: common/docker-container (português (Brasil))
description: "Gerenciar contêineres Docker."
content_hash: 2e3e7919eb090ef70c4749987fd7153e4af21a5d
last_modified_at: 2023-09-20
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
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># docker container

Gerenciar contêineres Docker.
Mais informações: <https://docs.docker.com/engine/reference/commandline/container/>.

- Listar os contêineres Docker em execução:

`docker container ls`

- Iniciar um ou mais contêineres parados:

`docker container start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_contêiner1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_contêiner2</span>

- Encerrar um ou mais contêineres em execução:

`docker container kill `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_contêiner</span>

- Parar um ou mais contêineres em execução:

`docker container stop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_contêiner</span>

- Pausar todos os processos em um ou mais contêineres:

`docker container pause `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_contêiner</span>

- Exibir informações detalhadas sobre um ou mais contêineres:

`docker container inspect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_contêiner</span>

- Exportar o sistema de arquivos de um contêiner como um arquivo tar:

`docker container export `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_contêiner</span>

- Criar uma nova imagem a partir das alterações em um contêiner:

`docker container commit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_contêiner</span>

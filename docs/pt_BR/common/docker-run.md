---
layout: page
title: common/docker-run (português (Brasil))
description: "Executa um comando em um novo container Docker."
content_hash: da34a9f6dc773e6484ecaef89a7e04ae6e18541e
last_modified_at: 2024-09-26
related_topics:
  - title: Deutsch version
    url: /de/common/docker-run.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-run.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-run.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/docker-run.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker-run.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/docker-run.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># docker run

Executa um comando em um novo container Docker.
Mais informações: <https://docs.docker.com/reference/cli/docker/container/run/>.

- Executa um comando em um novo container de uma imagem tagueada:

`docker run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imagem:tag</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>

- Executa um comando em um novo container em background e exibe o ID:

`docker run --detach `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Executa um comando em um novo container que será removido após a execução em um modo interativo e com um terminal TTY:

`docker run --rm --interactive --tty `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Executa um comando em um novo container com variáveis de ambiente:

`docker run --env '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variável</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">valor</span>`' --env `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variável</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imagem</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>

- Executa um comando em um novo container montando volumes nos caminhos específicos:

`docker run --volume `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/no/host_local</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/no/container</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imagem</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>

- Executa um comando em um novo container e abre as portas para acesso:

`docker run --publish `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">porta_do_host_local</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">porta_do_container</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imagem</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>

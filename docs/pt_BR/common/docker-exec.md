---
layout: page
title: common/docker-exec (português (Brasil))
description: "Executar um comando em um contêiner Docker em execução."
content_hash: 986f5a11a381919ed1d8db4ff5b1302431f00df3
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/docker-exec.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-exec.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-exec.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/docker-exec.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker-exec.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker exec

Executar um comando em um contêiner Docker em execução.
Mais informações: <https://docs.docker.com/engine/reference/commandline/exec/>.

- Entrar em uma sessão de shell interativa em um contêiner em execução:

`docker exec --interactive --tty `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_contêiner</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/bin/bash</span>

- Executar um comando em segundo plano (detached) em um contêiner em execução:

`docker exec --detach `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_contêiner</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>

- Selecionar o diretório de trabalho para a execução de um determinado comando:

`docker exec --interactive --tty --workdir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/diretório</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_contêiner</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>

- Executar um comando em segundo plano em um contêiner existente, mas manter o `stdin` aberto:

`docker exec --interactive --detach `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_contêiner</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>

- Definir uma variável de ambiente em uma sessão Bash em execução:

`docker exec --interactive --tty --env `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_da_variável</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">valor</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_contêiner</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/bin/bash</span>

- Executar um comando como um usuário específico:

`docker exec --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usuário</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_contêiner</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>

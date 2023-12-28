---
layout: page
title: common/podman (português (Brasil))
description: "Ferramenta de gerenciamento simples para pods, contêineres e imagens."
content_hash: 628817dceab7b298ff630a0d2611fb0ac5697c15
last_modified_at: 2023-12-28
related_topics:
  - title: English version
    url: /en/common/podman.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/podman.html
    icon: bi bi-globe
tldri18n_status: 2
---
# podman

Ferramenta de gerenciamento simples para pods, contêineres e imagens.
O Podman fornece uma linha de comando comparável ao Docker-CLI. Simplificando: `alias docker=podman`.
Mais informações: <https://github.com/containers/podman/blob/main/commands-demo.md>.

- Lista todos os contêineres (em execução e parados):

`podman ps --all`

- Cria um contêiner a partir de uma imagem, com um nome personalizado:

`podman run --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_contêiner</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imagem</span>

- Inicia ou para um contêiner existente:

`podman `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">start|stop</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_contêiner</span>

- Baixa uma imagem de um registro (por padrão, Docker Hub):

`podman pull `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imagem</span>

- Exibe a lista de imagens já baixadas:

`podman images`

- Abre um shell dentro de um contêiner que já está em execução:

`podman exec --interactive --tty `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_contêiner</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sh</span>

- Remove um contêiner parado:

`podman rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_contêiner</span>

- Exibe os logs de um ou mais contêineres e acompanha a saída do log:

`podman logs --follow `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_contêiner</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_do_contêiner</span>

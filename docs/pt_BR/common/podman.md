---
layout: page
title: common/podman (português (Brasil))
description: "Ferramenta de gerenciamento simples para pods, contêineres e imagens."
content_hash: 545a79385ef1077f439423c6cb0529891bef231d
last_modified_at: 2023-09-18
related_topics:
  - title: English version
    url: /en/common/podman.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/podman.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># podman

Ferramenta de gerenciamento simples para pods, contêineres e imagens.
O Podman fornece uma linha de comando comparável ao Docker-CLI. Simplificando: `alias docker=podman`.
Mais informações: <https://github.com/containers/podman/blob/main/commands-demo.md>.

- Listar todos os contêineres (em execução e parados):

`podman ps --all`

- Criar um contêiner a partir de uma imagem, com um nome personalizado:

`podman run --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_contêiner</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imagem</span>

- Iniciar ou parar um contêiner existente:

`podman `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">start|stop</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_contêiner</span>

- Baixar uma imagem de um registro (por padrão, Docker Hub):

`podman pull `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imagem</span>

- Exibir a lista de imagens já baixadas:

`podman images`

- Abrir um shell dentro de um contêiner que já está em execução:

`podman exec --interactive --tty `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_contêiner</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sh</span>

- Remover um contêiner parado:

`podman rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_contêiner</span>

- Exibir os logs de um ou mais contêineres e acompanhar a saída do log:

`podman logs --follow `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_contêiner</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_do_contêiner</span>

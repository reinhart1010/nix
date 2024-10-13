---
layout: page
title: common/podman-compose (português (Brasil))
description: "Executar e gerenciar definição de contêineres Compose Specification."
content_hash: 123b5707c894886e58e2ca32a122ac3b79068935
last_modified_at: 2024-10-13
related_topics:
  - title: English version
    url: /en/common/podman-compose.html
    icon: bi bi-globe
tldri18n_status: 2
---
# podman-compose

Executar e gerenciar definição de contêineres Compose Specification.
Mais informações: <https://github.com/containers/podman-compose>.

- Lista todos os contêineres em execução:

`podman-compose ps`

- Cria e inicia todos os contêineres em segundo plano usando um arquivo `docker-compose.yml` local:

`podman-compose up -d`

- Inicia todos os contêineres, fazendo o build se necessário:

`podman-compose up --build`

- Inicia todos os contêineres usando um arquivo de composição alternativo:

`podman-compose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-f|--file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>` up`

- Para todos os contêineres em execução:

`podman-compose stop`

- Remove todos os contêineres, redes e volumes:

`podman-compose down --volumes`

- Acompanha logs de um contêiner (omite todos os nomes de contêineres):

`podman-compose logs --follow `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_contêiner</span>

- Executa um comando único em um serviço sem mapear portas:

`podman-compose run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_serviço</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>

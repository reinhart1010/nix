---
layout: page
title: common/podman-compose (português (Brasil))
description: "Executar e gerenciar definição de contêineres Compose Specification."
content_hash: 387e2054760d423cf389efe0299ef85099eef93d
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/podman-compose.html
    icon: bi bi-globe
tldri18n_status: 2
---
# podman-compose

Executar e gerenciar definição de contêineres Compose Specification.
Mais informações: <https://github.com/containers/podman-compose>.

- Listar todos os contêineres em execução:

`podman-compose ps`

- Criar e iniciar todos os contêineres em segundo plano usando um arquivo `docker-compose.yml` local:

`podman-compose up -d`

- Iniciar todos os contêineres, fazendo o build se necessário:

`podman-compose up --build`

- Iniciar todos os contêineres usando um arquivo de composição alternativo:

`podman-compose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>` up`

- Parar todos os contêineres em execução:

`podman-compose stop`

- Remover todos os contêineres, redes e volumes:

`podman-compose down --volumes`

- Acompanhar logs de um contêiner (omitir todos os nomes de contêineres):

`podman-compose logs --follow `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_contêiner</span>

- Executar um comando único em um serviço sem mapear portas:

`podman-compose run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_serviço</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>

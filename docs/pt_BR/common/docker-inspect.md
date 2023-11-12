---
layout: page
title: common/docker-inspect (português (Brasil))
description: "Retorna informações de baixo nível sobre objetos do Docker."
content_hash: 79c678b84af3fb85b8a4280e17bfb7b4629266b3
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/docker-inspect.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-inspect.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-inspect.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/docker-inspect.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker-inspect.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker inspect

Retorna informações de baixo nível sobre objetos do Docker.
Mais informações: <https://docs.docker.com/engine/reference/commandline/inspect/>.

- Exibir ajuda:

`docker inspect`

- Exibir informações sobre um contêiner, imagem ou volume usando um nome ou ID:

`docker inspect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">contêiner|imagem|ID</span>

- Exibir o endereço IP de um contêiner:

`docker inspect --format='`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">range .NetworkSettings.Networks</span><span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.IPAddress</span><span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">end</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">contêiner</span>

- Exibir o caminho para o arquivo de log do contêiner:

`docker inspect --format='`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.LogPath</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">contêiner</span>

- Exibir o nome da imagem do contêiner:

`docker inspect --format='`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.Config.Image</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">contêiner</span>

- Exibir as informações de configuração como JSON:

`docker inspect --format='`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">json .Config</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">contêiner</span>

- Exibir todas as portas vinculadas:

`docker inspect --format='`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">range $p, $conf := .NetworkSettings.Ports</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$p</span>` -> `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">(index $conf 0).HostPort</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">end</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">contêiner</span>

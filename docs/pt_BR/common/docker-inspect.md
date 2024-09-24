---
layout: page
title: common/docker-inspect (português (Brasil))
description: "Retorna informações de baixo nível sobre objetos do Docker."
content_hash: 8da77c84067fe99b40894212f0f1905358c25324
last_modified_at: 2024-09-24
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
Mais informações: <https://docs.docker.com/reference/cli/docker/inspect/>.

- Exibe ajuda:

`docker inspect`

- Exibe informações sobre um contêiner, imagem ou volume usando um nome ou ID:

`docker inspect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">contêiner|imagem|ID</span>

- Exibe o endereço IP de um contêiner:

`docker inspect --format '\{\{range.NetworkSettings.Networks\}\}\{\{.IPAddress\}\}\{\{end\}\}' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">contêiner</span>

- Exibe o caminho para o arquivo de log do contêiner:

`docker inspect --format='\{\{.LogPath\}\}' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">contêiner</span>

- Exibe o nome da imagem do contêiner:

`docker inspect --format='\{\{.Config.Image\}\}' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">contêiner</span>

- Exibe as informações de configuração como JSON:

`docker inspect --format='\{\{json .Config\}\}' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">contêiner</span>

- Exibe todas as portas vinculadas:

`docker inspect --format='\{\{range $p, $conf := .NetworkSettings.Ports\}\} \{\{$p\}\} -> \{\{(index $conf 0).HostPort\}\} \{\{end\}\}' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">contêiner</span>

---
layout: page
title: common/docker-system (português (Brasil))
description: "Gerenciar dados do Docker e exibir informações do sistema em todo o sistema."
content_hash: 1e3cdfe8eb30f5ceb15c5ff63f5e28a29ba3505d
last_modified_at: 2024-04-19
related_topics:
  - title: Deutsch version
    url: /de/common/docker-system.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-system.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-system.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/docker-system.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker-system.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker system

Gerenciar dados do Docker e exibir informações do sistema em todo o sistema.
Mais informações: <https://docs.docker.com/engine/reference/commandline/system/>.

- Mostra ajuda:

`docker system`

- Mostra o uso de disco do Docker:

`docker system df`

- Mostra informações detalhadas sobre o uso de disco:

`docker system df --verbose`

- Remove dados não utilizados:

`docker system prune`

- Remove dados não utilizados criados há mais de um período específico no passado:

`docker system prune --filter "until=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">horas</span>`h`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">minutos</span>`m"`

- Exibe eventos em tempo real do daemon do Docker:

`docker system events`

- Exibe eventos em tempo real de contêineres transmitidos como JSON Lines válidos:

`docker system events --filter 'type=container' --format '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">json .</span>`'`

- Exibe informações em todo o sistema:

`docker system info`

---
layout: page
title: common/docker-system (português (Brasil))
description: "Gerenciar dados do Docker e exibir informações do sistema em todo o sistema."
content_hash: 4c0524b57c83752fa142274da8937368d846016b
last_modified_at: 2023-09-20
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
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># docker system

Gerenciar dados do Docker e exibir informações do sistema em todo o sistema.
Mais informações: <https://docs.docker.com/engine/reference/commandline/system/>.

- Mostrar ajuda:

`docker system`

- Mostrar o uso de disco do Docker:

`docker system df`

- Mostrar informações detalhadas sobre o uso de disco:

`docker system df --verbose`

- Remover dados não utilizados:

`docker system prune`

- Remover dados não utilizados criados há mais de um período específico no passado:

`docker system prune --filter="until=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">horas</span>`h`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">minutos</span>`m"`

- Exibir eventos em tempo real do daemon do Docker:

`docker system events`

- Exibir eventos em tempo real de contêineres transmitidos como JSON Lines válidos:

`docker system events --filter 'type=container' --format '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">json .</span>`'`

- Exibir informações em todo o sistema:

`docker system info`
---
layout: page
title: common/docker-network (italiano)
description: "Crea e gestisci reti docker."
content_hash: 9c5933bfdade873d1ee9b583e52b7d2a42e3ad1c
last_modified_at: 2024-03-14
related_topics:
  - title: Deutsch version
    url: /de/common/docker-network.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-network.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-network.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-network.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker-network.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker network

Crea e gestisci reti docker.
Maggiori informazioni: <https://docs.docker.com/engine/reference/commandline/network/>.

- Elenca le reti disponibili configurate sul Docker daemon:

`docker network ls`

- Crea una rete definita da un utente:

`docker network create --driver `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_del_driver</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_rete</span>

- Mostra informazioni dettagliate su una lista di reti (separata da spazi):

`docker network inspect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_rete_1 nome_rete_2</span>

- Connetti un container ad una rete usando il suo nome o ID:

`docker network connect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_rete</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_container|ID</span>

- Disconnetti un container da una rete:

`docker network disconnect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_rete</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_container|ID</span>

- Elimina le reti inutilizzate (non referenziate da alcun container):

`docker network prune`

- Elimina una lista di reti (separata da spazi) inutilizzate:

`docker network rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_rete_1 nome_rete_2</span>

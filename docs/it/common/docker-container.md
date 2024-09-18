---
layout: page
title: common/docker-container (italiano)
description: "Gestisci container Docker."
content_hash: 723e9ec74513e9ea25643c125ab16d89d43eb8c1
last_modified_at: 2024-09-18
related_topics:
  - title: Deutsch version
    url: /de/common/docker-container.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-container.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-container.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/docker-container.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-container.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker container

Gestisci container Docker.
Maggiori informazioni: <https://docs.docker.com/reference/cli/docker/container/>.

- Elenca i container Docker attualmente in esecuzione:

`docker container ls`

- Avvia uno o più container fermi:

`docker container start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_container1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_container2</span>

- Termina uno o più container in esecuzione:

`docker container kill `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_container</span>

- Ferma uno o più container in esecuzione:

`docker container stop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_container</span>

- Sospendi tutti i processi dentro uno o più container:

`docker container pause `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_container</span>

- Mostra informazioni dettagliate su uno o più container:

`docker container inspect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_container</span>

- Esporta il filesystem di un container come archivio tar:

`docker container export `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_container</span>

- Crea una nuova immagine dai cambiamenti di un container:

`docker container commit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_container</span>

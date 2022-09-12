---
layout: page
title: common/docker-compose (italiano)
description: "Esegui e gestisci applicazioni Docker composte da più container."
content_hash: 74e8516a8fce4bb7cdbb1182e5280a78d3b3db45
related_topics:
  - title: Deutsch version
    url: /de/common/docker-compose.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-compose.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/docker-compose.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-compose.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/docker-compose.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-compose.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker-compose.html
    icon: bi bi-globe
---
# docker compose

Esegui e gestisci applicazioni Docker composte da più container.
Maggiori informazioni: <https://docs.docker.com/compose/reference/>.

- Elenca i container in esecuzione:

`docker compose ps`

- Crea ed avvia tutti i container in background utilizzando il file `docker-compose.yml` nella directory corrente:

`docker compose up -d`

- Avvia tutti i container, buildandoli di nuovo se necessario:

`docker compose up --build`

- Avvia tutti i container utilizzando un file compose alternativo:

`docker compose --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/a/file</span>` up`

- Ferma tutti i container in esecuzione:

`docker compose stop`

- Ferma e rimuovi tutti i container, reti, immagini e volumi:

`docker compose down`

- Segui i log di tutti i container:

`docker compose logs --follow`

- Segui i log di un container specifico:

`docker compose logs --follow `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_container</span>

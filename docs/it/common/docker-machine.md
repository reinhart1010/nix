---
layout: page
title: common/docker-machine (italiano)
description: "Crea e gestisci macchine che utilizzano Docker."
content_hash: 84edebd7299bea4e4be5fc1400c554355f9692c5
last_modified_at: 2024-05-23
related_topics:
  - title: Deutsch version
    url: /de/common/docker-machine.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-machine.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-machine.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/docker-machine.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-machine.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker-machine.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker-machine

Crea e gestisci macchine che utilizzano Docker.
Maggiori informazioni: <https://github.com/docker/machine>.

- Elenca macchine Docker in esecuzione:

`docker-machine ls`

- Crea una nuova macchina Docker con uno specifico nome:

`docker-machine create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome</span>

- Mostra lo stato di una macchina:

`docker-machine status `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome</span>

- Avvia una macchina:

`docker-machine start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome</span>

- Arresta una macchina:

`docker-machine stop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome</span>

- Ispeziona le informazioni su di una macchina:

`docker-machine inspect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome</span>

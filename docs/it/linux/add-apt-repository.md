---
layout: page
title: linux/add-apt-repository (italiano)
description: "Gestisce le definizioni di repository apt."
content_hash: c62c122974110d52b81d2e1b6724a34dd89555fe
last_modified_at: 2023-11-12
related_topics:
  - title: català version
    url: /ca/linux/add-apt-repository.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/add-apt-repository.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/add-apt-repository.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/add-apt-repository.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/add-apt-repository.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/add-apt-repository.html
    icon: bi bi-globe
tldri18n_status: 2
---
# add-apt-repository

Gestisce le definizioni di repository apt.
Maggiori informazioni: <https://manned.org/apt-add-repository>.

- Aggiunge un nuovo repository apt:

`add-apt-repository `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">identificativo_del_repository</span>

- Rimuove un repository apt:

`add-apt-repository --remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">identificativo_del_repository</span>

- Aggiorna la cache dei pacchetti dopo aver aggiunto un repository:

`add-apt-repository --update `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">identificativo_del_repository</span>

- Attiva i pacchetti sorgente:

`add-apt-repository --enable-source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">identificativo_del_repository</span>

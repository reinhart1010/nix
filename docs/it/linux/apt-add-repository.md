---
layout: page
title: linux/apt-add-repository (italiano)
description: "Gestisce le definizioni di repository APT."
content_hash: 1c951bec3ea2ae6998158dea4d04369c3ffccb89
last_modified_at: 2024-03-14
related_topics:
  - title: català version
    url: /ca/linux/apt-add-repository.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/apt-add-repository.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/apt-add-repository.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/apt-add-repository.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/apt-add-repository.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/apt-add-repository.html
    icon: bi bi-globe
  - title: ไทย version
    url: /th/linux/apt-add-repository.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/apt-add-repository.html
    icon: bi bi-globe
tldri18n_status: 2
---
# apt-add-repository

Gestisce le definizioni di repository APT.
Maggiori informazioni: <https://manpages.debian.org/latest/software-properties-common/apt-add-repository.1.html>.

- Aggiunge un nuovo repository APT:

`apt-add-repository `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">identificativo_del_repository</span>

- Rimuove un repository APT:

`apt-add-repository --remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">identificativo_del_repository</span>

- Aggiorna la cache dei pacchetti dopo aver aggiunto un repository:

`apt-add-repository --update `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">identificativo_del_repository</span>

- Attiva i pacchetti sorgente:

`apt-add-repository --enable-source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">identificativo_del_repository</span>

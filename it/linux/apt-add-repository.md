---
layout: page
title: linux/apt-add-repository (italiano)
description: "Gestisce le definizioni di repository apt."
content_hash: e5e3d775ee87a363c235bedd0e88575b7de0864d
related_topics:
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
  - title: 中文 version
    url: /zh/linux/apt-add-repository.html
    icon: bi bi-globe
---
# apt-add-repository

Gestisce le definizioni di repository apt.
Maggiori informazioni: <https://manpages.debian.org/latest/software-properties-common/apt-add-repository.1.html>.

- Aggiunge un nuovo repository apt:

`apt-add-repository `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">identificativo_del_repository</span>

- Rimuove un repository apt:

`apt-add-repository --remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">identificativo_del_repository</span>

- Aggiorna la cache dei pacchetti dopo aver aggiunto un repository:

`apt-add-repository --update `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">identificativo_del_repository</span>

- Attiva i pacchetti sorgente:

`apt-add-repository --enable-source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">identificativo_del_repository</span>

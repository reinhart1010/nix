---
layout: page
title: linux/add-apt-repository (Deutsch)
description: "Verwalte apt-Repository Definitionen."
content_hash: 85a531f911c527e66c4f00989af98f71a199f78d
related_topics:
  - title: English version
    url: /en/linux/add-apt-repository.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/add-apt-repository.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/add-apt-repository.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/add-apt-repository.html
    icon: bi bi-globe
---
# add-apt-repository

Verwalte apt-Repository Definitionen.
Weitere Informationen: <https://manned.org/apt-add-repository>.

- Füge ein neues apt-Repository hinzu:

`add-apt-repository `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository_spec</span>

- Entferne ein apt-Repository:

`add-apt-repository --remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository_spec</span>

- Aktualisiere den Paketcache nach dem Hinzufügen eines Repositories:

`add-apt-repository --update `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository_spec</span>

- Erlaube das Herunterladen von Quellpaketen aus dem Repository:

`add-apt-repository --enable-source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository_spec</span>

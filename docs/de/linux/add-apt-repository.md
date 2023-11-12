---
layout: page
title: linux/add-apt-repository (Deutsch)
description: "Verwalte apt-Repository-Definitionen."
content_hash: 8064bd1635294d1e9d3aca4a8f5efc6a8a29200f
last_modified_at: 2023-11-12
related_topics:
  - title: català version
    url: /ca/linux/add-apt-repository.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/add-apt-repository.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/add-apt-repository.html
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

Verwalte apt-Repository-Definitionen.
Weitere Informationen: <https://manned.org/apt-add-repository>.

- Füge ein neues apt-Repository hinzu:

`add-apt-repository `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository_spec</span>

- Entferne ein apt-Repository:

`add-apt-repository --remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository_spec</span>

- Aktualisiere den Paketcache nach dem Hinzufügen eines Repositories:

`add-apt-repository --update `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository_spec</span>

- Erlaube das Herunterladen von Quellpaketen aus dem Repository:

`add-apt-repository --enable-source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository_spec</span>

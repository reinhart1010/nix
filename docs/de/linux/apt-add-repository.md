---
layout: page
title: linux/apt-add-repository (Deutsch)
description: "Editiere die Repository-Listen."
content_hash: 12f4d10722029f3aa0c9abb48493acbe2f8a9113
last_modified_at: 2024-09-18
related_topics:
  - title: català version
    url: /ca/linux/apt-add-repository.html
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
  - title: italiano version
    url: /it/linux/apt-add-repository.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/apt-add-repository.html
    icon: bi bi-globe
  - title: ไทย version
    url: /th/linux/apt-add-repository.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/apt-add-repository.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/apt-add-repository.html
    icon: bi bi-globe
tldri18n_status: 2
---
# apt-add-repository

Editiere die Repository-Listen.
Weitere Informationen: <https://manned.org/apt-add-repository.1>.

- Füge ein neues Repository hinzu:

`apt-add-repository `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository_spec</span>

- Entferne ein Repository:

`apt-add-repository --remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository</span>

- Aktualisiere den Cache nachdem das Repository hinzugefügt wurde:

`apt-add-repository --update `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository</span>

- Aktiviere Source-Pakete:

`apt-add-repository --enable-source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository</span>

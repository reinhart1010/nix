---
layout: page
title: linux/apt-add-repository (Deutsch)
description: "Editiere die Repository-Listen."
content_hash: 3da1f5d54f16fb8c4b6005f52edcac2cc20e5a04
related_topics:
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
  - title: 中文 version
    url: /zh/linux/apt-add-repository.html
    icon: bi bi-globe
---
# apt-add-repository

Editiere die Repository-Listen.
Weitere Informationen: <https://manpages.debian.org/latest/software-properties-common/apt-add-repository.1.html>.

- Füge ein neues Repository hinzu:

`apt-add-repository `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository_spec</span>

- Entferne ein Repository:

`apt-add-repository --remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository</span>

- Aktualisiere den Cache nachdem das Repository hinzugefügt wurde:

`apt-add-repository --update `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository</span>

- Aktiviere Source Pakete:

`apt-add-repository --enable-source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository</span>

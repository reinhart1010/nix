---
layout: page
title: linux/add-apt-repository (English)
description: "Manages `apt` repository definitions."
content_hash: f8af472bf38add7c8da256a2f85257bb3e7b9b1f
last_modified_at: 2024-01-30
related_topics:
  - title: català version
    url: /ca/linux/add-apt-repository.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/add-apt-repository.html
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

Manages `apt` repository definitions.
More information: <https://manned.org/apt-add-repository>.

- Add a new `apt` repository:

`add-apt-repository `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository_spec</span>

- Remove an `apt` repository:

`add-apt-repository --remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository_spec</span>

- Update the package cache after adding a repository:

`add-apt-repository --update `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository_spec</span>

- Allow source packages to be downloaded from the repository:

`add-apt-repository --enable-source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository_spec</span>

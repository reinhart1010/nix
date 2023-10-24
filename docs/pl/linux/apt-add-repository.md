---
layout: page
title: linux/apt-add-repository (polski)
description: "Zarządzaj definicjami repozytoriów `apt`."
content_hash: 6643c50c5b81f42a29792295cb5c29b449092c9e
last_modified_at: 2023-10-24
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
  - title: italiano version
    url: /it/linux/apt-add-repository.html
    icon: bi bi-globe
  - title: ไทย version
    url: /th/linux/apt-add-repository.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/apt-add-repository.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># apt-add-repository

Zarządzaj definicjami repozytoriów `apt`.
Więcej informacji: <https://manpages.debian.org/latest/software-properties-common/apt-add-repository.1.html>.

- Dodaj nowe repozytorium `apt`:

`apt-add-repository `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">specyfikacja_repozytorium</span>

- Usuń repozytorium `apt`:

`apt-add-repository --remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">specyfikacja_repozytorium</span>

- Zaktualizuj pamięć podręczną pakietów po dodaniu repozytorium:

`apt-add-repository --update `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">specyfikacja_repozytorium</span>

- Pozwól na pobieranie pakietów źródłowych z podanego repozytorium:

`apt-add-repository --enable-source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">specyfikacja_repozytorium</span>

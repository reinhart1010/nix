---
layout: page
title: linux/apt-add-repository (polski)
description: "Zarządzaj definicjami repozytoriów `apt`."
content_hash: 01b7a9895ef5b948008996da5179fe39f4a39491
last_modified_at: 2024-09-18
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
  - title: українська version
    url: /uk/linux/apt-add-repository.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/apt-add-repository.html
    icon: bi bi-globe
tldri18n_status: 2
---
# apt-add-repository

Zarządzaj definicjami repozytoriów `apt`.
Więcej informacji: <https://manned.org/apt-add-repository.1>.

- Dodaj nowe repozytorium `apt`:

`apt-add-repository `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">specyfikacja_repozytorium</span>

- Usuń repozytorium `apt`:

`apt-add-repository --remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">specyfikacja_repozytorium</span>

- Zaktualizuj pamięć podręczną pakietów po dodaniu repozytorium:

`apt-add-repository --update `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">specyfikacja_repozytorium</span>

- Pozwól na pobieranie pakietów źródłowych z podanego repozytorium:

`apt-add-repository --enable-source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">specyfikacja_repozytorium</span>

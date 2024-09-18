---
layout: page
title: linux/aptitude (polski)
description: "Narzędzie zarządzania pakietami dla Debiana i Ubuntu."
content_hash: 0a6c68c5d3f5a8da2fdaa0700e7c045764412ce9
last_modified_at: 2024-09-18
related_topics:
  - title: català version
    url: /ca/linux/aptitude.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/aptitude.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/aptitude.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/aptitude.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/aptitude.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/aptitude.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/aptitude.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/aptitude.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/aptitude.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aptitude

Narzędzie zarządzania pakietami dla Debiana i Ubuntu.
Więcej informacji: <https://manned.org/aptitude.8>.

- Zaktualizuj listę dostępnych pakietów oraz wersji. Zalecane jest uruchomienie tego polecenia przed innymi poleceniami `aptitude`:

`aptitude update`

- Zainstaluj nowy pakiet i jego zależności:

`aptitude install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakiet</span>

- Wyszukaj pakiet:

`aptitude search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakiet</span>

- Wyszukaj zainstalowany pakiet (`?installed` jest terminem wyszukiwania w `aptitude`):

`aptitude search '?installed(`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakiet</span>`)'`

- Usuń pakiet i wszystkie pakiety zależne od niego:

`aptitude remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakiet</span>

- Zaktualizuj zainstalowane pakiety do najnowszej dostępnej wersji:

`aptitude upgrade`

- Zaktualizuj zainstalowane pakiety (jak robi `aptitude upgrade`) włącznie z usunięciem przestarzałych pakietów i instalacją dodatkowych pakietów w celu spełnienia zależności:

`aptitude full-upgrade`

- Ustaw zainstalowany pakiet jako wstrzymany, aby zapobiec jego automatycznym aktualizacjom:

`aptitude hold '?installed(`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakiet</span>`)'`

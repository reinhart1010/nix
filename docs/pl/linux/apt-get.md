---
layout: page
title: linux/apt-get (polski)
description: "Narzędzie do zarządzania pakietami Debiana i Ubuntu."
content_hash: d21dc7664c72e121e2f8e49ad69024532ce1bada
last_modified_at: 2024-09-18
related_topics:
  - title: العربية version
    url: /ar/linux/apt-get.html
    icon: bi bi-globe
  - title: català version
    url: /ca/linux/apt-get.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/apt-get.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/apt-get.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/apt-get.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/linux/apt-get.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/apt-get.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/apt-get.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/apt-get.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/apt-get.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/apt-get.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/apt-get.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/apt-get.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/apt-get.html
    icon: bi bi-globe
tldri18n_status: 2
---
# apt-get

Narzędzie do zarządzania pakietami Debiana i Ubuntu.
Szukaj pakietów używając `apt-cache`.
Więcej informacji: <https://manned.org/apt-get.8>.

- Zaktualizuj listę dostępnych pakietów oraz wersji (zalecane jest uruchomienie tego polecenia przed innymi poleceniami `apt-get`):

`apt-get update`

- Zainstaluj pakiet lub zaktualizuj go do najnowszej dostępnej wersji:

`apt-get install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakiet</span>

- Usuń pakiet:

`apt-get remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakiet</span>

- Usuń pakiet i jego pliki konfiguracyjne:

`apt-get purge `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakiet</span>

- Zaktualizuj wszystkie zainstalowane pakiety do ich najnowszych dostępnych wersji:

`apt-get upgrade`

- Wyczyść lokalne repozytorium - usuwa wszystkie pliki pakietów (`.deb`) z przerwanych pobrań które nie mogą już być pobrane:

`apt-get autoclean`

- Usuń wszystkie pakiety, które już nie są potrzebne:

`apt-get autoremove`

- Zaktualizuj zainstalowane pakiety (jak `upgrade`), ale usuń przestarzałe pakiety i zainstaluj dodatkowe pakiety, aby spełnić zależności:

`apt-get dist-upgrade`

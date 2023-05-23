---
layout: page
title: linux/apt (polski)
description: "Narzędzie do zarządzania pakietami dla dystrybucji bazujących na Debianie."
content_hash: 10653c2a07c4e208b25fbae9e5ec67979d7c1988
last_modified_at: 2023-05-23
related_topics:
  - title: العربية version
    url: /ar/linux/apt.html
    icon: bi bi-globe
  - title: বাংলা version
    url: /bn/linux/apt.html
    icon: bi bi-globe
  - title: català version
    url: /ca/linux/apt.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/apt.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/apt.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/apt.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/apt.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/apt.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/apt.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/linux/apt.html
    icon: bi bi-globe
  - title: മലയാളം version
    url: /ml/linux/apt.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/apt.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/apt.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/linux/apt.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/apt.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/apt.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/apt.html
    icon: bi bi-globe
---
# apt

Narzędzie do zarządzania pakietami dla dystrybucji bazujących na Debianie.
Zalecany zamiennik `apt-get` przy użyciu interaktywnym w Ubuntu w wersjach 16.04 i wyższych.
Odpowiednie polecenia dla innych menedżerów pakietów: <https://wiki.archlinux.org/title/Pacman/Rosetta>.
Więcej informacji: <https://manpages.debian.org/latest/apt/apt.8.html>.

- Zaktualizuj listę dostępnych pakietów i ich wersji (zaleca się uruchomienie tego przed innymi poleceniami `apt`):

`sudo apt update`

- Wyszukaj podany pakiet:

`apt search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakiet</span>

- Wyświetl informacje o podanym pakiecie:

`apt show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakiet</span>

- Zainstaluj pakiet lub zaktualizuj go do najnowszej dostępnej wersji:

`sudo apt install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakiet</span>

- Usuń pakiet (użyj `purge` aby usunąć także pliki konfiguracyjne):

`sudo apt remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakiet</span>

- Zaktualizuj wszystkie zainstalowane pakiety do ich najnowszych wersji:

`sudo apt upgrade`

- Wyświetl wszystkie pakiety:

`apt list`

- Wyświetl zainstalowane pakiety:

`apt list --installed`

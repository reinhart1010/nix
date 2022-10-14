---
layout: page
title: linux/apt (polski)
description: "Narzędzie do zarządzania pakietami dla dystrybucji bazujących na Debianie."
content_hash: 5677902263509aac3b821ff5c1b54e44519771e7
related_topics:
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
  - title: മലയാളം version
    url: /ml/linux/apt.html
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

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># apt

Narzędzie do zarządzania pakietami dla dystrybucji bazujących na Debianie.
Zalecany zamiennik `apt-get` przy uyciu interaktywnym w Ubuntu w wersji 16.04 i wyższych.
Więcej informacji: <https://manpages.debian.org/latest/apt/apt.8.html>.

- Aktualizacja listy dostępnych pakietów i ich wersji (zalecane uruchomienie przed innymi poleceniami `apt`):

`sudo apt update`

- Wyszukanie podanego pakietu:

`apt search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakiet</span>

- Wyświetlenie informacji o pakiecie:

`apt show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakiet</span>

- Instalacja pakietu lub aktualizacja do najnowszej dostępnej wersji:

`sudo apt install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakiet</span>

- Usunięcie pakietu (użyj `purge` aby usunąć także pliki konfiguracyjne):

`sudo apt remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakiet</span>

- Aktualizacja wszystkich zainstalowanych pakietów do ich najnowszych wersji:

`sudo apt upgrade`

- Wyświetlenie wszystkich pakietów:

`apt list`

- Wyświetlenie zainstalowanych pakietów:

`apt list --installed`

---
layout: page
title: linux/pacman-query (polski)
description: "Narzędzie do zarządzania pakietami w Arch Linuksie."
content_hash: 64844d4ec99d1adf446b1427d4d30edb8330ac4f
last_modified_at: 2024-09-25
related_topics:
  - title: Deutsch version
    url: /de/linux/pacman-query.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/pacman-query.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/pacman-query.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/pacman-query.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/pacman-query.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/pacman-query.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pacman --query

Narzędzie do zarządzania pakietami w Arch Linuksie.
Zobacz także: `pacman`.
Więcej informacji: <https://manned.org/pacman.8>.

- Wyświetl zainstalowane pakiety i ich wersje:

`pacman --query`

- Wyświetl tylko pakiety niebędące zależnościami i ich wersje:

`pacman --query --explicit`

- Znajdź, do którego pakietu należy plik:

`pacman --query --owns `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa_pliku</span>

- Wyświetl informacje o zainstalowanym pakiecie:

`pacman --query --info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa_pakietu</span>

- Znajdź pliki należące do pakietu:

`pacman --query --list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa_pakietu</span>

- Wyświetl pakiety-sieroty (zainstalowane jako zależności ale nie są już wymagane przez żaden pakiet):

`pacman --query --unrequired --deps --quiet`

- Wyświetl zainstalowane pakiety, których nie ma w repozytoriach:

`pacman --query --foreign`

- Wyświetl przestarzałe pakiety:

`pacman --query --upgrades`

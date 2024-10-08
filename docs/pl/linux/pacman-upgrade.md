---
layout: page
title: linux/pacman-upgrade (polski)
description: "Narzędzie do zarządzania pakietami w Arch Linuksie."
content_hash: e77c8471062d987e6b8200fede87073122b91141
last_modified_at: 2024-09-25
related_topics:
  - title: Deutsch version
    url: /de/linux/pacman-upgrade.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/pacman-upgrade.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/pacman-upgrade.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/pacman-upgrade.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/pacman-upgrade.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/pacman-upgrade.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pacman --upgrade

Narzędzie do zarządzania pakietami w Arch Linuksie.
Zobacz także: `pacman`.
Więcej informacji: <https://manned.org/pacman.8>.

- Zainstaluj jeden lub więcej pakietów z plików:

`sudo pacman --upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pakietu1.pkg.tar.zst</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pakietu2.pkg.tar.zst</span>

- Zainstaluj pakiet bez pytania:

`sudo pacman --upgrade --noconfirm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pakietu.pkg.tar.zst</span>

- Nadpisz pliki będące w konflikcie podczas instalacji pakietów:

`sudo pacman --upgrade --overwrite `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pakietu.pkg.tar.zst</span>

- Zainstaluj pakiet, pomijając sprawdzanie wersji zależności:

`sudo pacman --upgrade --nodeps `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pakietu.pkg.tar.zst</span>

- Wyświetl pakiety, na które wpływ miałaby komenda (nie instaluje żadnych pakietów):

`pacman --upgrade --print `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pakietu.pkg.tar.zst</span>

- Wyświetl pomoc:

`pacman --upgrade --help`

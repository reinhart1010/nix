---
layout: page
title: linux/pacman-database (polski)
description: "Operuj na bazie danych pakietów Arch Linuksa."
content_hash: 986aa8a94da91e465d73dce12036d5db5b3c7105
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/linux/pacman-database.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/pacman-database.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/pacman-database.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/pacman-database.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pacman --database

Operuj na bazie danych pakietów Arch Linuksa.
Modyfikuj niektóre atrybuty zainstalowanych pakietów.
Zobacz także: `pacman`.
Więcej informacji: <https://man.archlinux.org/man/pacman.8>.

- Oznacz pakiet jako pośrednio zainstalowany (zależność):

`sudo pacman --database --asdeps `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa_pakietu</span>

- Oznacz pakiet jako bezpośrednio zainstalowany:

`sudo pacman --database --asexplicit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa_pakietu</span>

- Sprawdź, czy wszystkie zależności pakietów są zainstalowane:

`pacman --database --check`

- Sprawdź repozytoria, aby zapewnić, że wszystkie podane zależności są dostępne:

`pacman --database --check --check`

- Wyświetlaj tylko komunikaty o błędach:

`pacman --database --check --quiet`

- Wyświetl pomoc:

`pacman --database --help`

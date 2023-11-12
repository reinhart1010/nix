---
layout: page
title: linux/pacman-deptest (polski)
description: "Sprawdź każdą podaną zależność i zwróć listę zależności, które nie są aktualnie spełnione."
content_hash: 84815488ea4ede04b6d69dcce4324a8fe737bc8b
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/linux/pacman-deptest.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/pacman-deptest.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/pacman-deptest.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/pacman-deptest.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pacman --deptest

Sprawdź każdą podaną zależność i zwróć listę zależności, które nie są aktualnie spełnione.
Zobacz także: `pacman`.
Więcej informacji: <https://man.archlinux.org/man/pacman.8>.

- Wyświetl nazwy zależności, które nie są zainstalowane:

`pacman --deptest `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa_pakietu1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa_pakietu2</span>

- Sprawdź, czy zainstalowany pakiet spełnia podaną minimalną wersję:

`pacman --deptest "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bash>=5</span>`"`

- Sprawdź, czy jest zainstalowana nowsza wersja pakietu:

`pacman --deptest "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bash>5</span>`"`

- Wyświetl pomoc:

`pacman --deptest --help`

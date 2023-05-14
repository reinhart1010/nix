---
layout: page
title: linux/pacman-remove (polski)
description: "Narzędzie do zarządzania pakietami w Arch Linuksie."
content_hash: 5883a4a39e7c1b119a1308909d97c1525a33b8ef
last_modified_at: 2023-05-14
related_topics:
  - title: Deutsch version
    url: /de/linux/pacman-remove.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/pacman-remove.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/pacman-remove.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/pacman-remove.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/pacman-remove.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/pacman-remove.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># pacman --remove

Narzędzie do zarządzania pakietami w Arch Linuksie.
Zobacz także: `pacman`.
Więcej informacji: <https://man.archlinux.org/man/pacman.8>.

- Usuń pakiet i jego zależności:

`sudo pacman --remove --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa_pakietu</span>

- Usuń pakiet, jego zależności i pliki konfiguracyjne:

`sudo pacman --remove --recursive --nosave `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa_pakietu</span>

- Usuń pakiet bez pytania:

`sudo pacman --remove --noconfirm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa_pakietu</span>

- Usuń pakiety-sieroty (zainstalowane jako zależności ale nie są już wymagane przez żaden pakiet):

`sudo pacman --remove --recursive --nosave $(pacman --query --unrequired --deps --quiet)`

- Usuń pakiet i wszystke pakiety, które od niego zależą:

`sudo pacman --remove --cascade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa_pakietu</span>

- Wyświetl pakiety, na które wpływ miałaby komenda (nie usuwa żadnych pakietów):

`pacman --remove --print `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa_pakietu</span>

- Wyświetl pomoc dla tej komendy:

`pacman --remove --help`

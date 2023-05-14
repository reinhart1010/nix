---
layout: page
title: linux/pacman-files (polski)
description: "Narzędzie do zarządzania pakietami w Arch Linuksie."
content_hash: c71da61f99988c5495ce69206604efb7b30ea711
last_modified_at: 2023-05-14
related_topics:
  - title: Deutsch version
    url: /de/linux/pacman-files.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/pacman-files.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/pacman-files.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/pacman-files.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># pacman --files

Narzędzie do zarządzania pakietami w Arch Linuksie.
Zobacz także: `pacman`, `pkgfile`.
Więcej informacji: <https://man.archlinux.org/man/pacman.8>.

- Zaktualizuj bazę danych pakietów:

`sudo pacman --files --refresh`

- Znajdź pakiet, do którego należy podany plik:

`pacman --files `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa_pliku</span>

- Znajdź pakiet, do którego należy podany plik, używając wyrażenia regularnego:

`pacman --files --regex '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wyrażenie_regularne</span>`'`

- Wyświetl tylko nazwy pakietów:

`pacman --files --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa_pliku</span>

- Wyświetl pliki należące do podanego pakietu:

`pacman --files --list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa_pakietu</span>

- Wyświetl pomoc:

`pacman --files --help`

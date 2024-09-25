---
layout: page
title: linux/pacman-key (polski)
description: "Skrypt opakowujący dla GnuPG używany do zarządzania pękiem kluczy pacmana."
content_hash: 1753bfb2fc46455d8dbf95cf56b18c1d09153acb
last_modified_at: 2024-09-25
related_topics:
  - title: English version
    url: /en/linux/pacman-key.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/pacman-key.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/pacman-key.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/pacman-key.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pacman-key

Skrypt opakowujący dla GnuPG używany do zarządzania pękiem kluczy pacmana.
Zobacz także: `pacman`.
Więcej informacji: <https://manned.org/pacman-key>.

- Zainicjalizuj pęk kluczy pacmana:

`sudo pacman-key --init`

- Dodaj domyślne klucze Arch Linuksa:

`sudo pacman-key --populate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archlinux</span>

- Wyświetl klucze z pęku publicznego:

`pacman-key --list-keys`

- Dodaj podane klucze:

`sudo pacman-key --add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/klucza.gpg</span>

- Pobierz klucz z serwera kluczy:

`sudo pacman-key --recv-keys "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uid|imię|email</span>`"`

- Wyświetl odcisk podanego klucza:

`pacman-key --finger "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uid|imię|email</span>`"`

- Podpisz zaimportowany klucz lokalnie:

`sudo pacman-key --lsign-key "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uid|imię|email</span>`"`

- Usuń podany klucz:

`sudo pacman-key --delete "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uid|imię|email</span>`"`

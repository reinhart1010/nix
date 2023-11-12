---
layout: page
title: linux/pacman-database (Deutsch)
description: "Mit der Arch Linux Paketdatenbank arbeiten."
content_hash: d9f32b577825052b160d514a614d0da1e1f07c55
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/pacman-database.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/pacman-database.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/pacman-database.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/pacman-database.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pacman --database

Mit der Arch Linux Paketdatenbank arbeiten.
Verschiedene Attribute von installierten Paketen bearbeiten.
Siehe auch: `pacman`.
Weitere Informationen: <https://man.archlinux.org/man/pacman.8>.

- Markiere ein Paket als implizit installiert:

`sudo pacman --database --asdeps `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paketname</span>

- Markiere ein Paket als explizit installiert:

`sudo pacman --database --asexplicit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paketname</span>

- Überprüfe, dass alle Paketabhängigkeiten installiert sind:

`pacman --database --check`

- Überprüfe in den Repositorien, dass alle angegebenen Abhängigkeiten verfügbar sind:

`pacman --database --check --check`

- Zeige nur Fehlermeldungen:

`pacman --database --check --quiet`

- Zeige Hilfe an:

`pacman --database --help`

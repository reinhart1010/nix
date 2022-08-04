---
layout: page
title: linux/pacman-query (Deutsch)
description: "Arch Linux Paketverwaltungs-Werkzeug."
content_hash: b253339b9a0f63445cb8d72c51b9bc0522cdeb8c
related_topics:
  - title: English version
    url: /en/linux/pacman-query.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/pacman-query.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/pacman-query.html
    icon: bi bi-globe
---
# pacman --query

Arch Linux Paketverwaltungs-Werkzeug.
Weitere Informationen: <https://man.archlinux.org/man/pacman.8>.

- Liste alle installierten Pakete und dessen Versionen auf:

`pacman --query`

- Liste alle ausdrücklich installierten Pakete und dessen Versionen auf:

`pacman --query --explicit`

- Finde heraus welches Paket eine Datei besitzt:

`pacman --query --owns `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dateiname</span>

- Zeige Informationen über ein installiertes Paket an:

`pacman --query --info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paketname</span>

- Liste alle Dateien auf welche einem Paket gehören:

`pacman --query --list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paketname</span>

- Liste verwaiste Pakete auf (Pakete welche als Abhängigkeit installiert wurden, aber von keinem Paket benötigt werden):

`pacman --query --unrequired --deps --quiet`

- Liste installierte Pakete auf welche nicht in den Repositorien gefunden werden können:

`pacman --query --foreign`

- Liste veraltete Pakete auf:

`pacman --query --upgrades`

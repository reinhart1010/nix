---
layout: page
title: linux/pacman-database (Nederlands)
description: "Werk op de database van het Arch Linux pakket."
content_hash: 0c1561e2e0667b9b1374c1f8f3bbcbd2646c06f2
last_modified_at: 2025-01-04
related_topics:
  - title: Deutsch version
    url: /de/linux/pacman-database.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/pacman-database.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/pacman-database.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/pacman-database.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/pacman-database.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/pacman-database.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/pacman-database.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/pacman-database.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pacman --database

Werk op de database van het Arch Linux pakket.
Wijzig bepaalde attributen van de geïnstalleerde pakketten.
Bekijk ook: `pacman`.
Meer informatie: <https://manned.org/pacman.8>.

- Markeer een pakket als impliciet geïnstalleerd:

`sudo pacman -D --asdeps `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakket</span>

- Markeer een pakket als expliciet geïnstalleerd:

`sudo pacman -D --asexplicit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakket</span>

- Chec[k] dat alle pakket-afhankelijkheden zijn geïnstalleerd:

`pacman -Dk`

- Chec[k] de sync [D]atabase om ervoor te zorgen dat alle gespecificeerde afhankelijkheden van downloadbare pakketten beschikbaar zijn:

`pacman -Dkk`

- Chec[k] en toon in stille ([q]) modus (alleen foutmeldingen worden weergegeven):

`pacman -Dkq`

- Toon de [h]elp:

`pacman -Dh`

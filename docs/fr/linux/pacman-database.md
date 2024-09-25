---
layout: page
title: linux/pacman-database (français)
description: "Interagis avec les bases de données des paquets Arch Linux."
content_hash: a94bd566b1a64035bba374149b8efc93cbfb1da6
last_modified_at: 2024-09-25
related_topics:
  - title: Deutsch version
    url: /de/linux/pacman-database.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/pacman-database.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/pacman-database.html
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

Interagis avec les bases de données des paquets Arch Linux.
Modifie des attributs des paquets installés.
Voir aussi: `pacman`.
Plus d'informations : <https://manned.org/pacman.8>.

- Marque un paquet comme étant installé en tant que dépendance :

`sudo pacman --database --asdeps `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquet</span>

- Marque un paquet comme étant explicitement installé :

`sudo pacman --database --asexplicit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquet</span>

- Vérifie les dépendances de tous les paquets installés :

`pacman --database --check`

- Vérifie que toutes les dépendances des paquets installés sont disponibles dans les dépôts :

`pacman --database --check --check`

- N'affiche que les messages d'erreur :

`pacman --database --check --quiet`

- Affiche l'aide :

`pacman --database --help`

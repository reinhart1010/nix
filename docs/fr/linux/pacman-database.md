---
layout: page
title: linux/pacman-database (français)
description: "Interagis avec les bases de données des paquets Arch Linux."
content_hash: 4968bd9d81f2087358eefc2da4e939d344e67500
related_topics:
  - title: Deutsch version
    url: /de/linux/pacman-database.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/pacman-database.html
    icon: bi bi-globe
---
# pacman --database

Interagis avec les bases de données des paquets Arch Linux.
Modifie des attributs des paquets installés.
Plus d'informations : <https://man.archlinux.org/man/pacman.8>.

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

---
layout: page
title: linux/pacman-files (français)
description: "Interagis avec les bases de données de fichiers."
content_hash: 895cd544b5484402ecb60f94b8388e201d30a675
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/linux/pacman-files.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/pacman-files.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/pacman-files.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/pacman-files.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pacman --files

Interagis avec les bases de données de fichiers.
Voir aussi: `pacman`, `pkgfile`.
Plus d'informations : <https://man.archlinux.org/man/pacman.8>.

- Mets à jour les bases de données des fichiers :

`sudo pacman --files --refresh`

- Trouve les paquets contenant un fichier spécifique :

`pacman --files `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fichier</span>

- Trouve les paquets contenant un fichier spécifique en utilisant une expression régulière :

`pacman --files --regex '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">expression_reguliere</span>`'`

- Liste uniquement les noms de paquets :

`pacman --files --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fichier</span>

- Liste les fichiers contenus dans un paquet :

`pacman --files --list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquet</span>

- Affiche l'aide :

`pacman --files --help`

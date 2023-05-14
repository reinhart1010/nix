---
layout: page
title: linux/pacman-files (français)
description: "Interagis avec les bases de données de fichiers."
content_hash: 895cd544b5484402ecb60f94b8388e201d30a675
last_modified_at: 2023-05-14
related_topics:
  - title: Deutsch version
    url: /de/linux/pacman-files.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/pacman-files.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/pacman-files.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/pacman-files.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pacman --files

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

---
layout: page
title: linux/pacman-sync (français)
description: "Synchronise les paquets."
content_hash: 5e848ac26949bc6d4bcf98845eb45291c0cbc8ad
related_topics:
  - title: Deutsch version
    url: /de/linux/pacman-sync.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/pacman-sync.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/pacman-sync.html
    icon: bi bi-globe
---
# pacman --sync

Synchronise les paquets.
Plus d'informations : <https://man.archlinux.org/man/pacman.8>.

- Installe un nouveau paquet :

`sudo pacman --sync `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquet</span>

- Synchronise et mettre à jour :

`sudo pacman --sync --refresh --sysupgrade`

- Synchronise, mets à jour et installe un paquet sans demander de confirmation :

`sudo pacman --sync --refresh --sysupgrade --noconfirm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquet</span>

- Recherche un paquet en utilisant un nom ou une expression régulière :

`pacman --sync --search "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">motif</span>`"`

- Affiche des informations sur un paquet :

`pacman --sync --info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquet</span>

- Ecris par dessus des fichiers pendant une mise à jour :

`sudo pacman --sync --refresh --sysupgrade --overwrite `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Synchronise et mets à jour les paquets, en ignorant un paquet (peut être utilisé plusieurs fois) :

`sudo pacman --sync --refresh --sysupgrade --ignore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquet</span>

- Supprime les fichiers concernant des paquets non installés et les dépôts supprimés du cache de pacman :

`sudo pacman --sync --clean`

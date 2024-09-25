---
layout: page
title: linux/pacman-sync (français)
description: "Synchronise les paquets."
content_hash: 2d0a421f8f45821fe0e7552164de13229516a6de
last_modified_at: 2024-09-25
related_topics:
  - title: Deutsch version
    url: /de/linux/pacman-sync.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/pacman-sync.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/pacman-sync.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/pacman-sync.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/pacman-sync.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/pacman-sync.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/pacman-sync.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pacman --sync

Synchronise les paquets.
Voir aussi: `pacman`.
Plus d'informations : <https://manned.org/pacman.8>.

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

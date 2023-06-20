---
layout: page
title: linux/pacman (français)
description: "Outil de gestion de paquets sur Arch Linux."
content_hash: 1895531e2a3c9437b5211c185600bc3c38f3f1ad
last_modified_at: 2023-06-20
related_topics:
  - title: Deutsch version
    url: /de/linux/pacman.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/pacman.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/pacman.html
    icon: bi bi-globe
  - title: മലയാളം version
    url: /ml/linux/pacman.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/pacman.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/pacman.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/linux/pacman.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/pacman.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/pacman.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/pacman.html
    icon: bi bi-globe
---
# pacman

Outil de gestion de paquets sur Arch Linux.
Voir aussi: `pacman-database`, `pacman-deptest`, `pacman-files`, `pacman-key`, `pacman-mirrors`, `pacman-query`, `pacman-remove`, `pacman-sync`, `pacman-upgrade`.
Plus d'informations : <https://man.archlinux.org/man/pacman.8>.

- Synchronise et mets à jour tous les paquets :

`sudo pacman -Syu`

- Installe un nouveau paquet :

`sudo pacman -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_paquet</span>

- Efface un paquet et ses dépendances :

`sudo pacman -Rs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_paquet</span>

- Recherche dans la base de données des paquets contenant un certain fichier :

`pacman -F "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_fichier</span>`"`

- Liste les paquets installés et leurs versions :

`pacman -Q`

- Liste seulement les paquets installés explicitement et leurs versions :

`pacman -Qe`

- Trouve à quel paquet un certain fichier appartient :

`pacman -Qo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fichier</span>

- Vide le cache des paquets pour libérer de l'espace :

`sudo pacman -Scc`

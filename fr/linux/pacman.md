---
layout: page
title: linux/pacman (français)
description: "Outil de gestion de paquets sur Arch Linux."
content_hash: 66458f3e4e0b389ccd31f5d6d8087bc1d8e60fb2
related_topics:
  - title: Deutsch version
    url: /de/linux/pacman.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/pacman.html
    icon: bi bi-globe
  - title: മലയാളം version
    url: /ml/linux/pacman.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/pacman.html
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
Certaines commandes comme `pacman sync` ont leur propre documentation.
Plus d'informations : <https://man.archlinux.org/man/pacman.8>.

- Synchronise et mets à jour tous les paquets :

`sudo pacman --sync --refresh --sysupgrade`

- Installe un nouveau paquet :

`sudo pacman --sync `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_paquet</span>

- Efface un paquet et ses dépendances :

`sudo pacman --remove --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_paquet</span>

- Recherche dans la base de données des paquets une expression régulière ou mot clé :

`pacman --sync --search "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">terme_recherche</span>`"`

- Liste les paquets installés et leurs versions :

`pacman --query`

- Liste seulement les paquets installés explicitement et leurs versions :

`pacman --query --explicit`

- Trouve à quel paquet un certain fichier appartient :

`pacman --query --owns `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fichier</span>

- Vide le cache des paquets pour libérer de l'espace :

`sudo pacman --sync --clean --clean`

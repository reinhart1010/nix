---
layout: page
title: linux/pacman-upgrade (français)
description: "Mets à jour ou ajoute des paquets au système."
content_hash: da8101c5811917438fdad36a4d0aa97c48f15da1
related_topics:
  - title: Deutsch version
    url: /de/linux/pacman-upgrade.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/pacman-upgrade.html
    icon: bi bi-globe
---
# pacman --upgrade

Mets à jour ou ajoute des paquets au système.
Plus d'informations : <https://man.archlinux.org/man/pacman.8>.

- Affiche l'aide :

`pacman --upgrade --help`

- Installe un ou des paquets depuis le système de fichiers :

`sudo pacman --upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/paquet1.pkg.tar.zst</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/paquet2.pkg.tar.zst</span>

- Installe un paquet silencieusement :

`sudo pacman --upgrade --noconfirm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/paquet.pkg.tar.zst</span>

- Ecris par dessus les fichiers en conflit pendant l'installation du paquet :

`sudo pacman --upgrade --overwrite `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/paquet.pkg.tar.zst</span>

- Installe un paquet sans vérifier les dépendances :

`sudo pacman --upgrade --nodeps `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/paquet.pkg.tar.zst</span>

- Affiche ce qui se passerait si la commande était exécutée mais sans agir :

`pacman --query --print `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/paquet.pkg.tar.zst</span>

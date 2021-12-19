---
layout: page
title: linux/pacman-query (français)
description: "Fais des requêtes dans la base de données des paquets installés."
content_hash: 6b6abda7248fa4007abc876b77806a86434a7379
related_topics:
  - title: Deutsch version
    url: /de/linux/pacman-query.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/pacman-query.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/pacman-query.html
    icon: bi bi-globe
---
# pacman --query

Fais des requêtes dans la base de données des paquets installés.
Plus d'informations : <https://man.archlinux.org/man/pacman.8>.

- Liste les paquets installés et leur version :

`pacman --query`

- Liste uniquement les paquets installés explicitement :

`pacman --query --explicit`

- Trouve le paquet propriétaire d'un fichier :

`pacman --query --owns `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fichier</span>

- Affiche des informations sur un paquet installé :

`pacman --query --info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquet</span>

- Liste les fichiers appartenant à un paquet :

`pacman --query --list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquet</span>

- Liste les paquets orphelins (installés en tant que dépendances mais requis par aucun paquet installé) :

`pacman --query --unrequired --deps --quiet`

- Liste les paquets installés ne se trouvant pas dans les dépôts :

`pacman --query --foreign`

- Liste les paquets périmés :

`pacman --query --upgrades`

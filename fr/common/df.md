---
layout: page
title: common/df (français)
description: "Montre un aperçu de l'utilisation de l'espace disque."
content_hash: ec48702d1d3d646b5b106a2eb70882094e84fc87
related_topics:
  - title: Deutsch version
    url: /de/common/df.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/df.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/df.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/df.html
    icon: bi bi-globe
---
# df

Montre un aperçu de l'utilisation de l'espace disque.
Plus d'informations : <https://www.gnu.org/software/coreutils/df>.

- Afficher tous les systèmes de fichiers et leur utilisation d'espace disque :

`df`

- Afficher tous les systèmes de fichiers et leur utilisation d'espace disque dans un format plus facilement :

`df -h`

- Afficher le système de fichiers et son utilisation d'espace disque rattaché au chemin donné :

`df `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier_ou_dossier</span>

- Afficher des statistiques sur le nombre d'inodes disponibles :

`df -i`

- Afficher les systèmes de fichiers sauf ceux de types spécifiques :

`df -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">squashfs</span>` -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tmpfs</span>

---
layout: page
title: linux/btrfs-filesystem (français)
description: "Gérer les systèmes de fichiers btrfs."
content_hash: 4871640693182fb9cd72b2a91e8e98223f6fd1a8
last_modified_at: 2022-12-29
related_topics:
  - title: English version
    url: /en/linux/btrfs-filesystem.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/btrfs-filesystem.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/btrfs-filesystem.html
    icon: bi bi-globe
---
# btrfs filesystem

Gérer les systèmes de fichiers btrfs.
Plus d'informations : <https://btrfs.readthedocs.io/en/latest/btrfs-filesystem.html>.

- Afficher l'utilisation du système de fichiers (affiche les informations détaillées si executé en tant que `root`) :

`btrfs filesystem usage `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/point_de_montage_btrfs</span>

- Afficher l'utilisation individuellement pour chaque périphérique :

`sudo btrfs filesystem show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/point_de_montage_btrfs</span>

- Défragmenter un fichier unique sur un système de fichiers btrfs (à éviter lorsqu'un agent de dé-duplication est en cours d'exécution) :

`sudo btrfs filesystem defragment -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier</span>

- Défragmenter récursivement un dossier (ne franchit pas la limite de sous-volume) :

`sudo btrfs filesystem defragment -v -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/dossier</span>

- Force la resynchronisation des blocs de données non écrits sur le ou les disques :

`sudo btrfs filesystem sync `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/point_de_montage_btrfs</span>

- Afficher un sommaire d'utilisation des disques pour les fichiers dans un dossier, récursivement :

`sudo btrfs filesystem du --summarize `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/dossier</span>

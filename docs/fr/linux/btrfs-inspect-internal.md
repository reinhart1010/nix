---
layout: page
title: linux/btrfs-inspect-internal (français)
description: "Recherche des informations internes concernant un système de fichier btrfs."
content_hash: 8cc7e08f2346554c230185151bec0ec2e7729491
last_modified_at: 2022-12-29
related_topics:
  - title: English version
    url: /en/linux/btrfs-inspect-internal.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/btrfs-inspect-internal.html
    icon: bi bi-globe
---
# btrfs inspect-internal

Recherche des informations internes concernant un système de fichier btrfs.
Plus d'informations : <https://btrfs.readthedocs.io/en/latest/btrfs-inspect-internal.html>.

- Afficher les informations du superbloc :

`sudo btrfs inspect-internal dump-super `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/partition</span>

- Afficher les informations sur les superblocs et toutes ses copies :

`sudo btrfs inspect-internal dump-super --all `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/partition</span>

- Afficher les meta-informations du système de fichiers :

`sudo btrfs inspect-internal dump-tree `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/partition</span>

- Afficher la liste des fichiers dans le `n`-ième inode :

`sudo btrfs inspect-internal inode-resolve `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/point_de_montage_btrfs</span>

- Afficher la liste des fichiers à une adresse logique donnée :

`sudo btrfs inspect-internal logical-resolve `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">addresse_logique</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/point_de_montage_btrfs</span>

- Afficher les statistiques concernant les arbres de racines, de domaines (extent), de sommes de contrôle (csum) et de système de fichiers :

`sudo btrfs inspect-internal tree-stats `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/partition</span>

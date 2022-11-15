---
layout: page
title: linux/btrfs-subvolume (français)
description: "Gestion des sous-volumes et instantanés btrfs."
content_hash: 1e3f8d927144fa2fc57e796dde2a001e95c9a56b
related_topics:
  - title: English version
    url: /en/linux/btrfs-subvolume.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/btrfs-subvolume.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/btrfs-subvolume.html
    icon: bi bi-globe
---
# btrfs subvolume

Gestion des sous-volumes et instantanés btrfs.
Plus d'information : <https://btrfs.readthedocs.io/en/latest/btrfs-subvolume.html>.

- Créer un nouveau sous-volume vide :

`sudo btrfs subvolume create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/nouveau_sous_volume</span>

- Lister tous les sous-volumes et instantanés du système de fichiers indiqué :

`sudo btrfs subvolume list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/systeme_de_fichiers_btrfs</span>

- Supprimer un sous-volume :

`sudo btrfs subvolume delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/sous_volume</span>

- Créer un instantané en lecture seule d'un sous-volume existant :

`sudo btrfs subvolume snapshot -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/sous_volume_source</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/sous_volume_cible</span>

- Créer un instantané en lecture et écriture d'un sous-volume existant :

`sudo btrfs subvolume snapshot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/sous_volume_source</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/sous_volume_cible</span>

- Afficher les informations détaillées d'un sous-volume :

`sudo btrfs subvolume show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/sous_volume</span>

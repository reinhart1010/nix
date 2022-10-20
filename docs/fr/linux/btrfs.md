---
layout: page
title: linux/btrfs (français)
description: "Un système de fichiers pour Linux basé sur le principe \"copy-on-write\" (COW)."
content_hash: eef6578c550390224fe2f0934a4847e8d168d752
related_topics:
  - title: English version
    url: /en/linux/btrfs.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/btrfs.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/btrfs.html
    icon: bi bi-globe
---
# btrfs

Un système de fichiers pour Linux basé sur le principe "copy-on-write" (COW).
Certaines commandes comme `btrfs device` ont leur propre documentation.
Plus d'informations : <https://btrfs.wiki.kernel.org/index.php/Manpage/btrfs>.

- Crée un sous-volume :

`sudo btrfs subvolume create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/le/sous-volume</span>

- Liste les sous-volumes :

`sudo btrfs subvolume list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/le/point/de/montage</span>

- Affiche les informations d'utilisation de l'espace :

`sudo btrfs filesystem df `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/le/point/de/montage</span>

- Active le quota :

`sudo btrfs quote enable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/le/sous-volume</span>

- Affiche le quota :

`sudo btrfs qgroup show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/le/sous-volume</span>

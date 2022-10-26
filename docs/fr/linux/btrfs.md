---
layout: page
title: linux/btrfs (français)
description: "Système de fichiers basé sur le principe de copie à l’écriture (\"copy-on-write\", souvent désigné par son sigle anglais COW) pour Linux."
content_hash: 3212c8b1597d4ae2977cbc84be0506c92d7a55b4
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

Système de fichiers basé sur le principe de copie à l’écriture ("copy-on-write", souvent désigné par son sigle anglais COW) pour Linux.
Certaines sous-commandes comme `btrfs device` ont leur propre documentation.
Plus d'informations : <https://btrfs.wiki.kernel.org/index.php/Manpage/btrfs>.

- Créer un sous-volume :

`sudo btrfs subvolume create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/sous_volume</span>

- Lister les sous-volumes :

`sudo btrfs subvolume list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/point_de_montage</span>

- Afficher les informations d'utilisation d'espace :

`sudo btrfs filesystem df `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/point_de_montage</span>

- Activer les quotas :

`sudo btrfs quota enable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/sous_volume</span>

- Afficher les quotas :

`sudo btrfs qgroup show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/sous_volume</span>

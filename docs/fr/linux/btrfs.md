---
layout: page
title: linux/btrfs (français)
description: "Système de fichiers basé sur le principe de copie à l’écriture (\"copy-on-write\", souvent désigné par son sigle anglais COW) pour Linux."
content_hash: 0a317b2b3a372052c9e7d2df465b45d187fdcae6
last_modified_at: 2024-10-05
related_topics:
  - title: English version
    url: /en/linux/btrfs.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/linux/btrfs.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/btrfs.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/btrfs.html
    icon: bi bi-globe
tldri18n_status: 2
---
# btrfs

Système de fichiers basé sur le principe de copie à l’écriture ("copy-on-write", souvent désigné par son sigle anglais COW) pour Linux.
Certaines sous-commandes comme `device` ont leur propre documentation.
Plus d'informations : <https://btrfs.readthedocs.io/en/latest/btrfs.html>.

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

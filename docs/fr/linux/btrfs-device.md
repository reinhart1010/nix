---
layout: page
title: linux/btrfs-device (français)
description: "Gestion des partitions dans un système de fichiers BTRFS."
content_hash: 5c699c94a1762b4046748974ac608310c2156cea
related_topics:
  - title: English version
    url: /en/linux/btrfs-device.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/btrfs-device.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/btrfs-device.html
    icon: bi bi-globe
---
# btrfs device

Gestion des partitions dans un système de fichiers BTRFS.
Plus d'information : <https://btrfs.readthedocs.io/en/latest/btrfs-device.html>.

- Ajouter un ou plusieurs périphériques à un système de fichiers btrfs :

`sudo btrfs device add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/block_device1</span>` [`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/block_device2</span>`] `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/systeme_de_fichiers_btrfs</span>

- Retirer un périphérique d'un système de fichiers btrfs :

`sudo btrfs device remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/peripherique|identifiant_peripherique</span>` [`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">...</span>`]`

- Afficher les statistiques d'erreurs :

`sudo btrfs device stats `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/systeme_de_fichiers_btrfs</span>

- Scanner tous les disques et informer le noyau de tous les sytèmes de fichiers btrfs détectés :

`sudo btrfs device scan --all-devices`

- Afficher les statistiques détaillées d'allocation par disque :

`sudo btrfs device usage `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/systeme_de_fichiers_btrfs</span>

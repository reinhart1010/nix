---
layout: page
title: linux/btrfs-rescue (français)
description: "Essayer de récupérer un système de fichiers btrfs endommagé."
content_hash: aee77209733712996d2524729e223ccd827c3894
related_topics:
  - title: English version
    url: /en/linux/btrfs-rescue.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/btrfs-rescue.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># btrfs rescue

Essayer de récupérer un système de fichiers btrfs endommagé.
Plus d'informations : <https://btrfs.wiki.kernel.org/index.php/Manpage/btrfs-rescue>.

- Reconstruire les méta-données du système de fichiers (très lent) :

`sudo btrfs rescue chunk-recover `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/partition</span>

- Corriger les problèmes d'alignement de taille de périphérique (e.g. incohérence entre la taille du système de fichiers et le nombre total d'octets empéchant de monter la partition) :

`sudo btrfs rescue fix-device-size `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/partition</span>

- Restaurer un superbloc corrompu depuis ses copies correctes (restauration de la racine de l'arbre du système de fichiers) :

`sudo btrfs rescue super-recover `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/partition</span>

- Restaurer depuis des transactions interrompues (correction des problèmes de re-exécution des messages de journaux) :

`sudo btrfs rescue zero-log `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/partition</span>

- Créer un périphérique de contrôle sous `/dev/btrfs-control` quand l'outil `mknod` n'est pas installé :

`sudo btrfs rescue create-control-device`

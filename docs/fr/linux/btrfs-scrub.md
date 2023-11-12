---
layout: page
title: linux/btrfs-scrub (français)
description: "Éxaminer un système de fichiers btrfs pour vérifier l'intégrité de ses données."
content_hash: 201941a5679b43acf996545846f3ede1a19a232f
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/btrfs-scrub.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/btrfs-scrub.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/btrfs-scrub.html
    icon: bi bi-globe
tldri18n_status: 2
---
# btrfs scrub

Éxaminer un système de fichiers btrfs pour vérifier l'intégrité de ses données.
Il est recommandé de faire tourner une vérification tous les mois.
Plus d'informations : <https://btrfs.readthedocs.io/en/latest/btrfs-scrub.html>.

- Démarrer un examen :

`sudo btrfs scrub start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/point_de_montage_btrfs</span>

- Afficher le statut d'un examen en cours, ou du dernier examen complété :

`sudo btrfs scrub status `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/point_de_montage_btrfs</span>

- Stopper un examen en cours :

`sudo btrfs scrub cancel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/point_de_montage_btrfs</span>

- Reprendre un examen précédemment stoppé :

`sudo btrfs scrub resume `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/point_de_montage_btrfs</span>

- Démarrer un examen, mais attendre qu'il termine avant de rendre la main :

`sudo btrfs scrub start -B `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/point_de_montage_btrfs</span>

- Démarrer un examen en mode silencieux (n'affiche ni erreurs ni statistiques) :

`sudo btrfs scrub start -q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/le/point_de_montage_btrfs</span>

---
layout: page
title: linux/btrfs-check (français)
description: "Vérifier l'état, ou réparer un système de fichiers de type btrfs."
content_hash: 8830cb45dfb996cf899be94effea5843650403b6
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/btrfs-check.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/btrfs-check.html
    icon: bi bi-globe
tldri18n_status: 2
---
# btrfs check

Vérifier l'état, ou réparer un système de fichiers de type btrfs.
Plus d'informations : <https://btrfs.readthedocs.io/en/latest/btrfs-check.html>.

- Vérifier l'état d'un système de fichiers btrfs :

`sudo btrfs check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/partition</span>

- Vérifier l'état et réparer d'un système de fichiers btrfs (dangereux) :

`sudo btrfs check --repair `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/partition</span>

- Afficher la progression de vérification en cours :

`sudo btrfs check --progress `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/partition</span>

- Vérifier la somme de contrôle de chaque bloc de données (si le système de fichiers à été correctement vérifié) :

`sudo btrfs check --check-data-csum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/partition</span>

- Utiliser le `n`-ième super-bloc (`n` peut-être `0`, `1` ou `2`) :

`sudo btrfs check --super `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/partition</span>

- Reconstruire l'arbre des sommes de contrôle (checksum tree) :

`sudo btrfs check --repair --init-csum-tree `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/partition</span>

- Reconstruire l'arbre des domaines (extent tree) :

`sudo btrfs check --repair --init-extent-tree `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/partition</span>

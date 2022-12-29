---
layout: page
title: linux/btrfs-restore (français)
description: "Tenter de récupérer des fichiers depuis un système de fichiers btrfs endommagé."
content_hash: 844e0ff175d30e699447319f2b3673f6efbdd93f
last_modified_at: 2022-12-29
related_topics:
  - title: English version
    url: /en/linux/btrfs-restore.html
    icon: bi bi-globe
---
# btrfs restore

Tenter de récupérer des fichiers depuis un système de fichiers btrfs endommagé.
Plus d'informations : <https://btrfs.readthedocs.io/en/latest/btrfs-restore.html>.

- Restaurer tout les fichiers depuis un système de fichier btrfs vers un répertoire cible indiqué :

`sudo btrfs restore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/peripherique_btrfs</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/dossier</span>

- Lister (sans écriture) les fichiers qui peuvent être récupérés depuis un système de fichiers btrfs :

`sudo btrfs restore --dry-run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/du/device/btrfs</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/du/dossier</span>

- Restaurer les fichiers correspondants à une expression régulière donnée (non sensible à la casse) à restaurer depuis un système de fichiers btrfs (tous les répertoires parents des fichiers doivent correspondre également à l'expression régulière) :

`sudo btrfs restore --path-regex `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">expression_reguliere</span>` -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/peripherique_btrfs</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/dossier</span>

- Restaurer les fichiers depuis un système de fichiers btrfs en utilisant un arbre racine spécifique `bytenr` (voir `btrfs-find-root`) :

`sudo btrfs restore -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bytenr</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/peripherique_btrfs</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/dossier</span>

- Restaurer les fichiers depuis un système de fichiers btrfs (avec métadonnées, attributs étendus, et liens symboliques) en écrivant par dessus les fichiers déjà existants dans le répertoire cible :

`sudo btrfs restore --metadata --xattr --symlinks --overwrite `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/peripherique_btrfs</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/dossier</span>

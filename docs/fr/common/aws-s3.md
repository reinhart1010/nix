---
layout: page
title: common/aws-s3 (français)
description: "CLI pour AWS S3 - fournis du stockage à travers les services web."
content_hash: e88dcb40ddf33a26ef526c5e23eb1b16c7081bbc
related_topics:
  - title: Deutsch version
    url: /de/common/aws-s3.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/aws-s3.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/aws-s3.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/aws-s3.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/aws-s3.html
    icon: bi bi-globe
---
# aws s3

CLI pour AWS S3 - fournis du stockage à travers les services web.
Plus d'informations : <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3/index.html>.

- Affiche les fichiers d'un bucket :

`aws s3 ls `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_du_bucket</span>

- Synchronise les fichiers et dossiers locaux avec un bucket :

`aws s3 sync `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/les/fichiers</span>` s3://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_du_bucket</span>

- Synchronise les fichiers et dossiers d'un bucket avec le ceux en local :

`aws s3 sync s3://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_du_bucket</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/cible</span>

- Synchronise les fichiers et les dossiers avec des exclusions :

`aws s3 sync `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/les/fichiers</span>` s3://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_du_bucket</span>` --exclude `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/le/fichier</span>` --exclude `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/le/dossier</span>`/*`

- Supprime un fichier d'un bucket :

`aws s3 rm s3://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bucket</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/le/fichier</span>

- Prévisualise uniquement les changements :

`aws s3 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n_importe_quelle_commande</span>` --dryrun`

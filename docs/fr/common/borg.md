---
layout: page
title: common/borg (français)
description: "Outil de sauvegarde avec dé-duplication."
content_hash: b2bb5710123f256e0e7f91da90384367119511a1
related_topics:
  - title: Deutsch version
    url: /de/common/borg.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/borg.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/borg.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/borg.html
    icon: bi bi-globe
---
# borg

Outil de sauvegarde avec dé-duplication.
Crée des sauvegardes distantes ou locales qui peuvent être montées comme un système de fichiers.
Plus d'informations : <https://borgbackup.readthedocs.io/en/stable/usage/general.html>.

- Initialise un dépôt local :

`borg init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/chemin/vers/repertoire_du_depot</span>

- Sauvegarde un répertoire dans le dépôt en créant une archive appelée "Lundi" :

`borg create --progress `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/chemin/vers/repertoire_du_depot</span>`::`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Lundi</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/chemin/vers/repertoire_source</span>

- Liste toutes les archives d'un dépôt :

`borg list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/chemin/vers/repertoire_du_depot</span>

- Extrait un répertoire donné de l'archive nommée "Lundi" à partir d'un dépôt distant tout en excluant tous les fichiers *.ext :

`borg extract `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">utilisateur</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hote</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/chemin/vers/repertoire_du_depot</span>`::`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Lundi</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/repertoire_destination</span>` --exclude '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.ext</span>`'`

- Nettoie un dépôt en effaçant toutes les archives âgées de plus de 7 jours tout en affichant les changements :

`borg prune --keep-within `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">7d</span>` --list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/chemin/vers/repertoire_du_depot</span>

- Monte un dépôt comme un système de fichiers FUSE :

`borg mount `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/chemin/vers/repertoire_du_depot</span>`::`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Lundi</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/chemin/vers/point_de_montage</span>

- Affiche l'aide sur la création d'archives :

`borg create --help`

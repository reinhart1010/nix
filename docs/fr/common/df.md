---
layout: page
title: common/df (français)
description: "Montre un aperçu de l'utilisation de l'espace disque."
content_hash: a87a73e427aa8d98898c4ed3716f121d5ba5a642
last_modified_at: 2024-01-09
related_topics:
  - title: Deutsch version
    url: /de/common/df.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/df.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/df.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/df.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/df.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/df.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/df.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/df.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/df.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/df.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># df

Montre un aperçu de l'utilisation de l'espace disque.
Plus d'informations : <https://manned.org/df.1posix>.

- Afficher tous les systèmes de fichiers et leur utilisation d'espace disque :

`df`

- Afficher tous les systèmes de fichiers et leur utilisation d'espace disque dans un format plus facilement :

`df -h`

- Afficher le système de fichiers et son utilisation d'espace disque rattaché au chemin donné :

`df `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier_ou_dossier</span>

- Afficher des statistiques sur le nombre d'inodes disponibles :

`df -i`

- Afficher les systèmes de fichiers sauf ceux de types spécifiques :

`df -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">squashfs</span>` -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tmpfs</span>

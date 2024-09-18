---
layout: page
title: linux/apt-file (français)
description: "Recherche de fichiers dans les paquets APT, y compris ceux qui ne sont pas encore installés."
content_hash: 24cbf26ee84c9f39cc86ab2f566c1acb377c7529
last_modified_at: 2024-09-18
related_topics:
  - title: català version
    url: /ca/linux/apt-file.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/apt-file.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/apt-file.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/apt-file.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/apt-file.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/apt-file.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/apt-file.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/apt-file.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/apt-file.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/apt-file.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># apt-file

Recherche de fichiers dans les paquets APT, y compris ceux qui ne sont pas encore installés.
Plus d'informations : <https://manned.org/apt-file.1>.

- Mise à jour la base de données des métadonnées :

`sudo apt update`

- Recherche des paquets qui contiennent le fichier ou le chemin d'accès spécifié :

`apt-file search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">part/of/filename</span>

- Énumère le contenu d'un paquet spécifique :

`apt-file list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>

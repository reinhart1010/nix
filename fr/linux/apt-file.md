---
layout: page
title: linux/apt-file (français)
description: "Recherche de fichiers dans les paquets apt, y compris ceux qui ne sont pas encore installés."
content_hash: c57820598ee57af29b0ad62e3c96df0d346e8151
related_topics:
  - title: Deutsch version
    url: /de/linux/apt-file.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/apt-file.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/apt-file.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/apt-file.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/apt-file.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/apt-file.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/apt-file.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># apt-file

Recherche de fichiers dans les paquets apt, y compris ceux qui ne sont pas encore installés.
Plus d'informations : <https://manpages.debian.org/latest/apt-file/apt-file.1.html>.

- Mise à jour la base de données des métadonnées :

`sudo apt update`

- Recherche des paquets qui contiennent le fichier ou le chemin d'accès spécifié :

`apt-file search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">part/of/filename</span>

- Énumère le contenu d'un paquet spécifique :

`apt-file list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>

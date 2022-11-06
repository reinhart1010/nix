---
layout: page
title: linux/alien (français)
description: "Convertit différents paquets d'installation vers d'autres formats :"
content_hash: 7bce6e5995ddafd36f3f31f84664b2792ffcffa9
related_topics:
  - title: Deutsch version
    url: /de/linux/alien.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/alien.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/alien.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/alien.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># alien

Convertit différents paquets d'installation vers d'autres formats :
Plus d'information : <https://manned.org/alien>.

- Convertit un fichier d'installation spécifique vers le format Debian (extension `.deb`) :

`sudo alien --to-deb `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier</span>

- Convertit un fichier d'installation spécifique vers le format Red Hat (extension `.rpm`) :

`sudo alien --to-rpm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier</span>

- Convertit un fichier d'installation spécifique en un fichier d'installation Slackware (extension `.tgz`) :

`sudo alien --to-tgz `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier</span>

- Convertit un fichier d'installation spécifique vers le format Debian et l'installe sur le système :

`sudo alien --to-deb --install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier</span>
---
layout: page
title: linux/alien (français)
description: "Convertit différents paquets d'installation vers d'autres formats :"
content_hash: 1e089afc5c8c78fdcede3f68c630131a03cd05ef
last_modified_at: 2022-12-29
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
# alien

Convertit différents paquets d'installation vers d'autres formats :
Plus d'informations : <https://manned.org/alien>.

- Convertit un fichier d'installation spécifique vers le format Debian (extension `.deb`) :

`sudo alien --to-deb `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier</span>

- Convertit un fichier d'installation spécifique vers le format Red Hat (extension `.rpm`) :

`sudo alien --to-rpm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier</span>

- Convertit un fichier d'installation spécifique en un fichier d'installation Slackware (extension `.tgz`) :

`sudo alien --to-tgz `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier</span>

- Convertit un fichier d'installation spécifique vers le format Debian et l'installe sur le système :

`sudo alien --to-deb --install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier</span>

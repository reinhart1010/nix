---
layout: page
title: linux/apk (français)
description: "Gestionnaire de paquet d'Alpine Linux."
content_hash: 53ddf75a6dbfad46ae710c5bc51948aabe74af18
related_topics:
  - title: Deutsch version
    url: /de/linux/apk.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/apk.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/apk.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/apk.html
    icon: bi bi-globe
---
# apk

Gestionnaire de paquet d'Alpine Linux.
Plus d'informations : <https://wiki.alpinelinux.org/wiki/Alpine_Linux_package_management>.

- Mets à jour les indexes de tous les dépôts distants :

`apk update`

- Installe un nouveau paquet :

`apk add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquet</span>

- Désinstalle un paquet :

`apk del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquet</span>

- Essaye de réparer un paquet ou de mettre à jour un paquet sans ses dépendances :

`apk fix `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquet</span>

- Recherche des paquets à partir d'un mot-clé :

`apk search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mot_cle</span>

- Obtiens des information à propos d'un paquet précis :

`apk info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquet</span>

---
layout: page
title: linux/apt-cache (français)
description: "Outil de recherche de paquets Debian et Ubuntu."
content_hash: 0b918b55edc72dded0afc96478156bdd932e1705
last_modified_at: 2023-11-12
related_topics:
  - title: català version
    url: /ca/linux/apt-cache.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/apt-cache.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/apt-cache.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/apt-cache.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/apt-cache.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/apt-cache.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/apt-cache.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/apt-cache.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/apt-cache.html
    icon: bi bi-globe
tldri18n_status: 2
---
# apt-cache

Outil de recherche de paquets Debian et Ubuntu.
Plus d'informations : <https://manpages.debian.org/latest/apt/apt-cache.8.html>.

- Recherche un paquet dans vos sources actuelles :

`apt-cache search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">query</span>

- Affiche des informations sur un paquet :

`apt-cache show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Indique si un paquet est installé et à jour :

`apt-cache policy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Affiche les dépendances d'un paquet :

`apt-cache depends `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Affiche les paquets qui dépendent d'un paquet particulier :

`apt-cache rdepends `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

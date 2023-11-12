---
layout: page
title: linux/apt-get (français)
description: "Utilitaire de gestion des paquets Debian et Ubuntu."
content_hash: f87a8a2c1c4cfbc117f7ed74a7e336d68e9fdd74
last_modified_at: 2023-11-12
related_topics:
  - title: العربية version
    url: /ar/linux/apt-get.html
    icon: bi bi-globe
  - title: català version
    url: /ca/linux/apt-get.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/apt-get.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/apt-get.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/apt-get.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/linux/apt-get.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/apt-get.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/apt-get.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/apt-get.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/apt-get.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/apt-get.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/apt-get.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/apt-get.html
    icon: bi bi-globe
tldri18n_status: 2
---
# apt-get

Utilitaire de gestion des paquets Debian et Ubuntu.
Recherche des paquets en utilisant `apt-cache`.
Plus d'informations : <https://manpages.debian.org/latest/apt/apt-get.8.html>.

- Mise à jour de la liste des paquets et des versions disponibles (il est recommandé de l'exécuter avant les autres commandes `apt-get`) :

`apt-get update`

- Installation d'un paquet, ou mise à jour avec la dernière version disponible :

`apt-get install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Suppression d'un paquet :

`apt-get remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Suppression d'un paquet et de ses fichiers de configuration :

`apt-get purge `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Mise à jour de tous les paquets installés vers les dernières versions disponibles :

`apt-get upgrade`

- Nettoyage du dépôt local - supprime les fichiers de paquets (`.deb`) des téléchargements interrompus qui ne peuvent plus être téléchargés :

`apt-get autoclean`

- Suppression de tous les paquets qui ne sont plus nécessaires :

`apt-get autoremove`

- Mise à jour des paquets installés (comme la commande `upgrade`), mais avec suppression des paquets obsolètes et installation des paquets supplémentaires pour répondre aux nouvelles dépendances :

`apt-get dist-upgrade`

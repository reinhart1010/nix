---
layout: page
title: linux/apt (français)
description: "Utilitaire de gestion des paquets pour les distributions basées sur Debian."
content_hash: d8ecde01c59935acac30b11fa750f258a8c472db
last_modified_at: 2024-09-18
related_topics:
  - title: العربية version
    url: /ar/linux/apt.html
    icon: bi bi-globe
  - title: বাংলা version
    url: /bn/linux/apt.html
    icon: bi bi-globe
  - title: català version
    url: /ca/linux/apt.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/apt.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/apt.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/apt.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/linux/apt.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/apt.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/apt.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/linux/apt.html
    icon: bi bi-globe
  - title: മലയാളം version
    url: /ml/linux/apt.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/apt.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/apt.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/apt.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/linux/apt.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/apt.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/apt.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/apt.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/apt.html
    icon: bi bi-globe
tldri18n_status: 2
---
# apt

Utilitaire de gestion des paquets pour les distributions basées sur Debian.
Remplacement recommandé pour `apt-get` lorsqu'il est utilisé de manière interactive dans les versions 16.04 et ultérieures d'Ubuntu.
Plus d'informations : <https://manned.org/apt.8>.

- Mettre à jour la liste des paquets et des versions disponibles (il est recommandé de l'exécuter avant les autres commandes `apt`) :

`sudo apt update`

- Recherche d'un paquet donné :

`apt search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Afficher les informations pour un paquet :

`apt show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Installer un paquet, ou le mettre à jour avec la dernière version disponible :

`sudo apt install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Supprimer un paquet (utiliser `purge` à la place supprime également ses fichiers de configuration) :

`sudo apt remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Mettre à jour tous les paquets installés vers les dernières versions disponibles :

`sudo apt upgrade`

- Lister tous les paquets :

`apt list`

- Lister les paquets installés :

`apt list --installed`

---
layout: page
title: linux/a2query (français)
description: "Retourne la configuration d'exécution d'Apache sur une distribution Debian."
content_hash: f3dc74eefaad14019247b783fae19f9d1d14508e
related_topics:
  - title: Deutsch version
    url: /de/linux/a2query.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/a2query.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/a2query.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/a2query.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/linux/a2query.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/a2query.html
    icon: bi bi-globe
---
# a2query

Retourne la configuration d'exécution d'Apache sur une distribution Debian.
Plus d'informations : <https://manpages.debian.org/buster/apache2/a2query.1.en.html>.

- Liste les [m]odules Apache actifs :

`sudo a2query -m`

- Vérifie si un module spécifique est installé :

`sudo a2query -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_module</span>

- Liste les hôtes virtuels actifs :

`sudo a2query -s`

- Affiche le [M]odule de traitement multiple actif :

`sudo a2query -M`

- Affiche la [v]ersion d'Apache :

`sudo a2query -v`

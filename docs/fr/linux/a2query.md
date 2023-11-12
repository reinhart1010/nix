---
layout: page
title: linux/a2query (français)
description: "Retourne la configuration d'exécution d'Apache sur une distribution Debian."
content_hash: 695cc9a7b5a367ede4bab327041b762f7771d97b
last_modified_at: 2023-11-12
related_topics:
  - title: català version
    url: /ca/linux/a2query.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/a2query.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/a2query.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/a2query.html
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
  - title: Türkçe version
    url: /tr/linux/a2query.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/a2query.html
    icon: bi bi-globe
tldri18n_status: 2
---
# a2query

Retourne la configuration d'exécution d'Apache sur une distribution Debian.
Plus d'informations : <https://manpages.debian.org/latest/apache2/a2query.html>.

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

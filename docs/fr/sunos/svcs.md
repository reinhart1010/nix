---
layout: page
title: sunos/svcs (français)
description: "Répertorier les informations sur les services en cours d'exécution."
content_hash: d797f484574234308c7409379b1617626ac2c82a
related_topics:
  - title: English version
    url: /en/sunos/svcs.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/sunos/svcs.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/sunos/svcs.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/sunos/svcs.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># svcs

Répertorier les informations sur les services en cours d'exécution.
Plus d'information : <https://www.unix.com/man-page/linux/1/svcs>.

- Lister tous les services en cours d'exécution :

`svcs`

- Lister les services qui ne fonctionnent pas :

`svcs -vx`

- Répertorier les informations sur un service :

`svcs apache`

- Afficher l'emplacement du fichier journal de service :

`svcs -L apache`

- Afficher la fin d'un fichier journal de service :

`tail $(svcs -L apache)`

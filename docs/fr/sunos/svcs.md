---
layout: page
title: sunos/svcs (français)
description: "Répertorier les informations sur les services en cours d'exécution."
content_hash: 6a968bf037b624b7ef4c760836518d153bcdf210
last_modified_at: 2023-11-12
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
tldri18n_status: 2
---
# svcs

Répertorier les informations sur les services en cours d'exécution.
Plus d'informations : <https://www.unix.com/man-page/linux/1/svcs>.

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

---
layout: page
title: sunos/prstat (français)
description: "Signaler les statistiques de processus actifs."
content_hash: 4f26c6757057650230ee55972e11b079f251dd4b
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/sunos/prstat.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/sunos/prstat.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/sunos/prstat.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/sunos/prstat.html
    icon: bi bi-globe
tldri18n_status: 2
---
# prstat

Signaler les statistiques de processus actifs.
Plus d'informations : <https://www.unix.com/man-page/sunos/1m/prstat>.

- Examinez tous les processus et rapportez les statistiques triées par utilisation du processeur :

`prstat`

- Examinez tous les processus et rapportez les statistiques triées par utilisation de la mémoire :

`prstat -s rss`

- Rapporter le résumé de l'utilisation totale pour chaque utilisateur :

`prstat -t`

- Rapporter les informations comptables du processus de micro-état :

`prstat -m`

- Imprimez une liste des 5 meilleurs processeurs utilisant des processus chaque seconde :

`prstat -c -n 5 -s cpu 1`

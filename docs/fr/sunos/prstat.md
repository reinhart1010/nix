---
layout: page
title: sunos/prstat (français)
description: "Signaler les statistiques de processus actifs."
content_hash: c690d529781747a09f9b9797aa86c8c2ee5c5a40
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
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># prstat

Signaler les statistiques de processus actifs.
Plus d'information : <https://www.unix.com/man-page/sunos/1m/prstat>.

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

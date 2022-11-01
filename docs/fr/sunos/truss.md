---
layout: page
title: sunos/truss (français)
description: "Outil de dépannage pour tracer les appels système."
content_hash: dbea8acb0a6cf9fe0bdeb81a909e99e1af0bdc7d
related_topics:
  - title: English version
    url: /en/sunos/truss.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/sunos/truss.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/sunos/truss.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/sunos/truss.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># truss

Outil de dépannage pour tracer les appels système.
Équivalent SunOS de strace.
Plus d'information : <https://www.unix.com/man-page/linux/1/truss>.

- Commencez à tracer un programme en l'exécutant, en suivant tous les processus enfants :

`truss -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">programme</span>

- Commencez à tracer un processus spécifique par son PID :

`truss -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- Commencez à tracer un programme en l'exécutant, en affichant les arguments et les variables d'environnement :

`truss -a -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">programme</span>

- Comptez le temps, les appels et les erreurs pour chaque appel système et rapportez un résumé à la sortie du programme :

`truss -c -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- Tracez une sortie de filtrage de processus par appel système :

`truss -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>` -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_d'appel_système</span>

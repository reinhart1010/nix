---
layout: page
title: sunos/truss (français)
description: "Outil de dépannage pour tracer les appels système."
content_hash: 5a378ec371d65c1dcda65024a1120c664035fd56
last_modified_at: 2022-12-29
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
# truss

Outil de dépannage pour tracer les appels système.
Équivalent SunOS de strace.
Plus d'informations : <https://www.unix.com/man-page/linux/1/truss>.

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

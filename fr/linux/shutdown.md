---
layout: page
title: linux/shutdown (français)
description: "Éteint et redémarre le système."
content_hash: 2d8d97955b70d1af71e777ee77eebb2eb08aeb82
related_topics:
  - title: English version
    url: /en/linux/shutdown.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/shutdown.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/shutdown.html
    icon: bi bi-globe
---
# shutdown

Éteint et redémarre le système.
Plus d'informations : <https://manned.org/shutdown.8>.

- Éteint (arrête) immédiatement :

`shutdown -h now`

- Redémarre immédiatement :

`shutdown -r now`

- Redémarre dans 5 minutes :

`shutdown -r +`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` &`

- Éteint à 1:00 pm (Utilise un format 24h) :

`shutdown -h 13:00`

- Annule une opération d'arrêt ou de redémarrage du système en attente :

`shutdown -c`

---
layout: page
title: linux/cfdisk (français)
description: "Un programme pour gérer les tables de partitions et les partitions sur un disque dur en utilisant une interface utilisateur de type \"curses\"."
content_hash: b12cf991bee219190b8f742da21eeafaee6af26f
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/linux/cfdisk.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/cfdisk.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/cfdisk.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cfdisk

Un programme pour gérer les tables de partitions et les partitions sur un disque dur en utilisant une interface utilisateur de type "curses".
Plus d'informations : <https://manned.org/cfdisk>.

- Lance le manipulateur de partitions sur un appareil spécifique :

`cfdisk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>

- Crée une nouvelle table de partitions pour un appareil spécifique et la gère :

`cfdisk --zero `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>

---
layout: page
title: sunos/dmesg (français)
description: "Écrire les messages du noyau sur la sortie standard."
content_hash: f2f91c23f86c484add394f47d1c601e77d2735f8
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/sunos/dmesg.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/sunos/dmesg.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/sunos/dmesg.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/sunos/dmesg.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/sunos/dmesg.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dmesg

Écrire les messages du noyau sur la sortie standard.
Plus d'informations : <https://www.unix.com/man-page/sunos/1m/dmesg>.

- Afficher les messages du noyau :

`dmesg`

- Afficher la quantité de mémoire physique disponible sur ce système :

`dmesg | grep -i memory`

- Afficher les messages du noyau une page à la fois :

`dmesg | less`

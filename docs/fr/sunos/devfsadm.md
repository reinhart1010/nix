---
layout: page
title: sunos/devfsadm (français)
description: "Commande d'administration pour `/dev`. Maintient le `/dev` espace de noms."
content_hash: 157d579069d698580541c03a2b591ec38ef929a0
related_topics:
  - title: English version
    url: /en/sunos/devfsadm.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/sunos/devfsadm.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/sunos/devfsadm.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/sunos/devfsadm.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># devfsadm

Commande d'administration pour `/dev`. Maintient le `/dev` espace de noms.
Plus d'information : <https://www.unix.com/man-page/sunos/1m/devfsadm>.

- Rechercher de nouveaux disques :

`devfsadm -c disk`

- Nettoyez tout pendaison `/dev` liens et rechercher un nouvel appareil :

`devfsadm -C -v`

- Marche à sec - sortir ce qui serait changé mais ne faire aucune modification :

`devfsadm -C -v -n`

---
layout: page
title: sunos/devfsadm (français)
description: "Commande d'administration pour `/dev`. Maintient le `/dev` espace de noms."
content_hash: cda7052d08b635275db74d98f627698ecef43eaa
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/sunos/devfsadm.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/sunos/devfsadm.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/sunos/devfsadm.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/sunos/devfsadm.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/sunos/devfsadm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# devfsadm

Commande d'administration pour `/dev`. Maintient le `/dev` espace de noms.
Plus d'informations : <https://www.unix.com/man-page/sunos/1m/devfsadm>.

- Rechercher de nouveaux disques :

`devfsadm -c disk`

- Nettoyez tout pendaison `/dev` liens et rechercher un nouvel appareil :

`devfsadm -C -v`

- Marche à sec - sortir ce qui serait changé mais ne faire aucune modification :

`devfsadm -C -v -n`

---
layout: page
title: linux/ip-route-show (français)
description: "Sous commande de gestion de l'affichage des tables de routage."
content_hash: 007ef49216047d67e372d29e16ce32599edf0408
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># ip route show

Sous commande de gestion de l'affichage des tables de routage.
Plus d'information : <https://manned.org/ip-route>.

- Affiche la table de routage :

`ip route show`

- Affiche la table de routage principale (identique au premier exemple) :

`ip route show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">main|254</span>

- Affiche la table de routage locale :

`ip route show table `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">local|255</span>

- Affiche l'ensemble des tables de routage :

`ip route show table `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">all|unspec|0</span>

- Affiche les routes d'un périphérique donné :

`ip route show dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>

- Affiche les routes d'une portée donnée :

`ip route show scope link`

- Affiche le cache de routage :

`ip route show cache`

- N'affiche que les routes IPv6 ou IPv4 :

`ip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-6|-4</span>` route show`

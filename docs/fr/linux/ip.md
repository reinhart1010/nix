---
layout: page
title: linux/ip (français)
description: "Affiche / manipule l'adressage, le routage, les interfaces et périphériques réseau, les règles de routage et les tunnels."
content_hash: 8743be6266c2a8d11ebe3228fa680e0ce75b33ea
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/linux/ip.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/ip.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/ip.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/ip.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/ip.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ip

Affiche / manipule l'adressage, le routage, les interfaces et périphériques réseau, les règles de routage et les tunnels.
Certaines commandes comme `ip address` ont leur propre documentation.
Plus d'informations : <https://www.man7.org/linux/man-pages/man8/ip.8.html>.

- Liste les interfaces avec des infos détaillées :

`ip address`

- Liste les interfaces sur la couche réseau de façon synthétique :

`ip -brief address`

- Liste les interfaces sur la couche liaison de façon synthétique :

`ip -brief link`

- Affiche la table de routage :

`ip route`

- Affiche les voisins (table ARP) :

`ip neighbour`

- Active/Désactive une interface :

`ip link set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface</span>` up/down`

- Ajoute/Supprime une adresse ip à une interface :

`ip addr add/del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mask</span>` dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface</span>

- Ajoute une route par défaut :

`ip route add default via `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip</span>` dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface</span>

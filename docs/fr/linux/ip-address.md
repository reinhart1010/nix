---
layout: page
title: linux/ip-address (français)
description: "Sous-commande de gestion des adresses IP."
content_hash: c501d1ffa914ae0eb6b9a2e3c10f132d3879ed84
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/linux/ip-address.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/ip-address.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/ip-address.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ip address

Sous-commande de gestion des adresses IP.
Plus d'informations : <https://manned.org/ip-address>.

- Liste les interfaces réseau et leurs adresses IP associées :

`ip address`

- Filtre pour n'afficher que les interfaces réseau actives :

`ip address show up`

- Affiche les informations relatives à une interface réseau spécifique :

`ip address show dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>

- Ajoute une adresse IP à une interface réseau :

`ip address add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_address</span>` dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>

- Supprimer une adresse réseau d'une interface réseau :

`ip address delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_address</span>` dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>

- Supprime l'ensemble des adresses IP sur une portée donnée (scope) depuis une interface réseau :

`ip address flush dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>` scope `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">global|host|link</span>

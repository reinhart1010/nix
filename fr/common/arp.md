---
layout: page
title: common/arp (français)
description: "Affiche et manipule votre cache système ARP."
content_hash: 127d34576cf18b91d31ba1a7b3b084a2f47f74f4
related_topics:
  - title: English version
    url: /en/common/arp.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/arp.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/arp.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/arp.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/arp.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/arp.html
    icon: bi bi-globe
---
# arp

Affiche et manipule votre cache système ARP.
Plus d'informations : <https://manned.org/arp>.

- Affiche la table ARP courante :

`arp -a`

- Nettoie le cache :

`sudo arp -a -d`

- Supprime une entrée spécifique :

`arp -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">adresse</span>

- Crée une entré dans la table ARP:

`arp -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">adresse</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">adresse_mac</span>

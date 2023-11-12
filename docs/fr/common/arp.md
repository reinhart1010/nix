---
layout: page
title: common/arp (français)
description: "Affiche et manipule votre cache système ARP."
content_hash: 6e58f4fa87cea8e06bfbb5853ba523af731df8bb
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/arp.html
    icon: bi bi-globe
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
  - title: Türkçe version
    url: /tr/common/arp.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/arp.html
    icon: bi bi-globe
tldri18n_status: 2
---
# arp

Affiche et manipule votre cache système ARP.
Plus d'informations : <https://manned.org/arp>.

- Affiche la table ARP courante :

`arp -a`

- Supprime une entrée spécifique :

`arp -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">adresse</span>

- Crée une entré dans la table ARP:

`arp -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">adresse</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">adresse_mac</span>

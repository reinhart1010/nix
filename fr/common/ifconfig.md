---
layout: page
title: common/ifconfig (français)
description: "Configurateur des interfaces réseau."
content_hash: 6a6e419759a072f5225b2355548bc1080cdc870a
related_topics:
  - title: English version
    url: /en/common/ifconfig.html
    icon: bi bi-globe
---
# ifconfig

Configurateur des interfaces réseau.
Plus d'informations : <https://net-tools.sourceforge.io/man/ifconfig.8.html>.

- Affiche les paramètres de réseau d'un adaptateur ethernet :

`ifconfig `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>

- Affiche les détails de toutes les interfaces, y compris les interfaces désactivées :

`ifconfig -a`

- Désactive l'interface eth0 :

`ifconfig `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>` down`

- Active l'interface eth0 :

`ifconfig `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>` up`

- Assigne une adresse IP à l'interface eth0 :

`ifconfig `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">addresse_ip</span>

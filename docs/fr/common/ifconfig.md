---
layout: page
title: common/ifconfig (français)
description: "Configurateur des interfaces réseau."
content_hash: 1ecf09795e856a94f11e19869882b983fac2d64e
last_modified_at: 2023-12-28
related_topics:
  - title: English version
    url: /en/common/ifconfig.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/ifconfig.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ifconfig

Configurateur des interfaces réseau.
Plus d'informations : <https://net-tools.sourceforge.io/man/ifconfig.8.html>.

- Affiche les paramètres de réseau d'un adaptateur ethernet :

`ifconfig eth0`

- Affiche les détails de toutes les interfaces, y compris les interfaces désactivées :

`ifconfig -a`

- Désactive l'interface eth0 :

`ifconfig eth0 down`

- Active l'interface eth0 :

`ifconfig eth0 up`

- Assigne une adresse IP à l'interface eth0 :

`ifconfig eth0 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">addresse_ip</span>

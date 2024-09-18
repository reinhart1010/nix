---
layout: page
title: linux/ifup (polski)
description: "Narzędzie używane do włączania interfejsów sieciowych."
content_hash: 2b549b14d03b4feff8c2eb6184a9e0be95421ebc
last_modified_at: 2024-09-18
related_topics:
  - title: English version
    url: /en/linux/ifup.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/ifup.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ifup

Narzędzie używane do włączania interfejsów sieciowych.
Więcej informacji: <https://manned.org/ifup.8>.

- Włączenie interfejsu eth0:

`ifup `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>

- Włączenie wszystkich interfejsów zdefiniowanych jako "auto" w `/etc/network/interfaces`:

`ifup -a`

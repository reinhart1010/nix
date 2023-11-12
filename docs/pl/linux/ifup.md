---
layout: page
title: linux/ifup (polski)
description: "Narzędzie używane do włączania interfejsów sieciowych."
content_hash: 7dc5be67f3eeae1e57dc6eaef32b4227d906b2f9
last_modified_at: 2023-11-12
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
Więcej informacji: <https://manpages.debian.org/latest/ifupdown/ifup.8.html>.

- Włączenie interfejsu eth0:

`ifup `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>

- Włączenie wszystkich interfejsów zdefiniowanych jako "auto" w `/etc/network/interfaces`:

`ifup -a`

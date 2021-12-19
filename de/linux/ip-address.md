---
layout: page
title: linux/ip-address (Deutsch)
description: "IP Adressen Management Unterbefehl."
content_hash: 39c4f97f3cdbf54ce7921b88436a32504d02ce9a
related_topics:
  - title: English version
    url: /en/linux/ip-address.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/ip-address.html
    icon: bi bi-globe
---
# ip address

IP Adressen Management Unterbefehl.
Weitere Informationen: <https://manned.org/ip-address>.

- Zeige Netzwerk-Interfaces mit ihren Adressen:

`ip address`

- Zeige nur die aktiven Netzwerk-Interfaces:

`ip address show up`

- Zeige Informationen über ein bestimmtes Interface:

`ip address show dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>

- Füge eine Adresse zu einem Interface hinzu:

`ip address add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_adresse</span>` dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>

- Entferne eine Adresse von einem Interface:

`ip address delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_adresse</span>` dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>

- Entfernt alle IP Adressen in einem speziellen Bereich von einem Interface:

`ip address flush dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>` scope `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">global|host|link</span>

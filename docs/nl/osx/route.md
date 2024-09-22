---
layout: page
title: osx/route (Nederlands)
description: "Manipuleer handmatig de routetabellen."
content_hash: b206f847f15b4ef7f32c508edf07cc246631e96d
last_modified_at: 2024-09-22
related_topics:
  - title: English version
    url: /en/osx/route.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/route.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/osx/route.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/route.html
    icon: bi bi-globe
tldri18n_status: 2
---
# route

Manipuleer handmatig de routetabellen.
Vereist rootrechten.
Meer informatie: <https://keith.github.io/xcode-man-pages/route.8.html>.

- Voeg een route toe naar een bestemming via een gateway:

`sudo route add "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bestemming_ip_adres</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gateway_adres</span>`"`

- Voeg een route toe naar een /24 subnet via een gateway:

`sudo route add "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subnet_ip_adres</span>`/24" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gateway_adres</span>`"`

- Voer uit in testmodus (doet niets, alleen afdrukken):

`sudo route -t add "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bestemming_ip_adres</span>`/24" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gateway_adres</span>`"`

- Verwijder alle routes:

`sudo route flush`

- Verwijder een specifieke route:

`sudo route delete "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bestemming_ip_adres</span>`/24"`

- Zoek en toon de route voor een bestemming (hostname of IP-adres):

`sudo route get "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bestemming</span>`"`

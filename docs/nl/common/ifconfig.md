---
layout: page
title: common/ifconfig (Nederlands)
description: "Netwerkinterface-configurator."
content_hash: 768d4af635bfb480e0185f257f8062d7e1bfa89c
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/ifconfig.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/ifconfig.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ifconfig.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ifconfig

Netwerkinterface-configurator.
Meer informatie: <https://net-tools.sourceforge.io/man/ifconfig.8.html>.

- Bekijk netwerkinstellingen van een interface:

`ifconfig `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface_naam</span>

- Toon details van alle interfaces, inclusief uitgeschakelde interfaces:

`ifconfig -a`

- Schakel een interface uit:

`ifconfig `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface_naam</span>` down`

- Schakel een interface in:

`ifconfig `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface_naam</span>` up`

- Ken een IP-adres toe aan een interface:

`ifconfig `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface_naam</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_adres</span>

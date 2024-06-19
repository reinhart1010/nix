---
layout: page
title: common/ifconfig (Nederlands)
description: "Netwerkinterface-configurator."
content_hash: 70cefe02a482f908768c6917c558b69a85462756
last_modified_at: 2024-06-19
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

- Bekijk netwerkinstellingen van een Ethernet-adapter:

`ifconfig eth0`

- Toon details van alle interfaces, inclusief uitgeschakelde interfaces:

`ifconfig -a`

- Schakel de eth0-interface uit:

`ifconfig eth0 down`

- Schakel de eth0-interface in:

`ifconfig eth0 up`

- Ken een IP-adres toe aan de eth0-interface:

`ifconfig eth0 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_adres</span>

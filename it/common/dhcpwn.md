---
layout: page
title: common/dhcpwn (italiano)
description: "Testa attacchi di esaurimento IP DHCP ed intercetta il traffico DHCP locale."
content_hash: 745f66012ccd4bbc813e73b1d47bb65447bdbf3a
related_topics:
  - title: English version
    url: /en/common/dhcpwn.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/dhcpwn.html
    icon: bi bi-globe
---
# dhcpwn

Testa attacchi di esaurimento IP DHCP ed intercetta il traffico DHCP locale.
Maggiori informazioni: <https://github.com/mschwager/dhcpwn>.

- Inonda la rete con richieste di IP:

`dhcpwn --interface `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interfaccia</span>` flood --count `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">numero_di_richieste</span>

- Intercetta traffico DHCP locale:

`dhcpwn --interface `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interfaccia</span>` sniff`

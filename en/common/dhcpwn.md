---
layout: page
title: common/dhcpwn (English)
description: "Test DHCP IP exhaustion attacks and sniff local DHCP traffic."
content_hash: 78eb1cd58c021fcbc2f1fbfd30245955903eaca9
related_topics:
  - title: italiano version
    url: /it/common/dhcpwn.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/dhcpwn.html
    icon: bi bi-globe
---
# dhcpwn

Test DHCP IP exhaustion attacks and sniff local DHCP traffic.
More information: <https://github.com/mschwager/dhcpwn>.

- Flood the network with IP requests:

`dhcpwn --interface `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">network_interface</span>` flood --count `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">number_of_requests</span>

- Sniff local DHCP traffic:

`dhcpwn --interface `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">network_interface</span>` sniff`

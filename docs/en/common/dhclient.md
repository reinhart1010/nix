---
layout: page
title: common/dhclient (English)
description: "DHCP client."
content_hash: 2d112f2e585b3d049dcf5e51908a3740a3a23123
last_modified_at: 2023-11-12
related_topics:
  - title: 한국어 version
    url: /ko/common/dhclient.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dhclient

DHCP client.
More information: <https://manned.org/dhclient>.

- Get an IP address for the `eth0` interface:

`sudo dhclient `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>

- Release an IP address for the `eth0` interface:

`sudo dhclient -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>

---
layout: page
title: linux/ufw (English)
description: "Uncomplicated Firewall."
content_hash: e26d4baeac1cb7970078c560a7dfe6ed4ba45bf3
last_modified_at: 2023-11-12
related_topics:
  - title: català version
    url: /ca/linux/ufw.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/ufw.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/ufw.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/ufw.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/ufw.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ufw

Uncomplicated Firewall.
Frontend for `iptables` aiming to make configuration of a firewall easier.
More information: <https://wiki.ubuntu.com/UncomplicatedFirewall>.

- Enable ufw:

`ufw enable`

- Disable ufw:

`ufw disable`

- Show ufw rules, along with their numbers:

`ufw status numbered`

- Allow incoming traffic on port 5432 on this host with a comment identifying the service:

`ufw allow `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5432</span>` comment "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Service</span>`"`

- Allow only TCP traffic from 192.168.0.4 to any address on this host, on port 22:

`ufw allow proto `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tcp</span>` from `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.0.4</span>` to `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">any</span>` port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">22</span>

- Deny traffic on port 80 on this host:

`ufw deny `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">80</span>

- Deny all UDP traffic to ports in range 8412:8500:

`ufw deny proto `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">udp</span>` from `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">any</span>` to `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">any</span>` port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8412:8500</span>

- Delete a particular rule. The rule number can be retrieved from the `ufw status numbered` command:

`ufw delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rule_number</span>

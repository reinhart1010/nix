---
layout: page
title: linux/iptables (English)
description: "Configure tables, chains and rules of the Linux kernel IPv4 firewall."
content_hash: de59b0f7b953f2a1ddf1310ab61a13e7ebb123c1
last_modified_at: 2023-11-12
related_topics:
  - title: italiano version
    url: /it/linux/iptables.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/iptables.html
    icon: bi bi-globe
tldri18n_status: 2
---
# iptables

Configure tables, chains and rules of the Linux kernel IPv4 firewall.
Use `ip6tables` to set rules for IPv6 traffic. See also: `iptables-save`, `iptables-restore`.
More information: <https://manned.org/iptables>.

- View chains, rules, packet/byte counters and line numbers for the filter table:

`sudo iptables --verbose --numeric --list --line-numbers`

- Set chain [P]olicy rule:

`sudo iptables --policy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chain</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rule</span>

- [A]ppend rule to chain policy for IP:

`sudo iptables --append `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chain</span>` --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip</span>` --jump `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rule</span>

- [A]ppend rule to chain policy for IP considering [p]rotocol and port:

`sudo iptables --append `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chain</span>` --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip</span>` --protocol `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tcp|udp|icmp|...</span>` --dport `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>` --jump `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rule</span>

- Add a NAT rule to translate all traffic from the `192.168.0.0/24` subnet to the host's public IP:

`sudo iptables --table `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nat</span>` --append `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">POSTROUTING</span>` --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.0.0/24</span>` --jump `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">MASQUERADE</span>

- [D]elete chain rule:

`sudo iptables --delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chain</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rule_line_number</span>

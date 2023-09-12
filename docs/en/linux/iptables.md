---
layout: page
title: linux/iptables (English)
description: "Program that allows configuration of tables, chains and rules provided by the Linux kernel firewall."
content_hash: a01188b55ee839046d3c5241732e2508d38dde33
last_modified_at: 2023-09-12
related_topics:
  - title: italiano version
    url: /it/linux/iptables.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/iptables.html
    icon: bi bi-globe
---
# iptables

Program that allows configuration of tables, chains and rules provided by the Linux kernel firewall.
More information: <https://www.netfilter.org/projects/iptables/>.

- View chains, rules, packet/byte counters and line numbers for the filter table:

`sudo iptables --verbose --numeric --list --line-numbers`

- Set chain [P]olicy rule:

`sudo iptables --policy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chain</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rule</span>

- [A]ppend rule to chain policy for IP:

`sudo iptables --append `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chain</span>` --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip</span>` --jump `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rule</span>

- [A]ppend rule to chain policy for IP considering [p]rotocol and port:

`sudo iptables --append `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chain</span>` --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip</span>` --protocol `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">protocol</span>` --dport `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>` --jump `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rule</span>

- Add a NAT rule to translate all traffic from the `192.168.0.0/24` subnet to the host's public IP:

`sudo iptables --table `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nat</span>` --append `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">POSTROUTING</span>` --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.0.0/24</span>` --jump `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">MASQUERADE</span>

- [D]elete chain rule:

`sudo iptables --delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chain</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rule_line_number</span>

- Save `iptables` configuration of a given [t]able to a file:

`sudo iptables-save --table `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tablename</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/iptables_file</span>

- Restore `iptables` configuration from a file:

`sudo iptables-restore < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/iptables_file</span>

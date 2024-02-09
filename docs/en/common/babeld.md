---
layout: page
title: common/babeld (English)
description: "Routing daemon for Babel which uses firewall-style filters."
content_hash: 6f345c357a10db9db1f19aea8d12c0b45b92f055
last_modified_at: 2024-02-09
related_topics:
  - title: Deutsch version
    url: /de/common/babeld.html
    icon: bi bi-globe
tldri18n_status: 2
---
# babeld

Routing daemon for Babel which uses firewall-style filters.
More information: <https://www.irif.fr/~jch/software/babel/babeld.html>.

- Start the daemon with one or more [c]onfiguration files (read in order):

`babeld -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/ports.conf</span>` -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/filters.conf</span>` -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/interfaces.conf</span>

- [D]eamonize after startup:

`babeld -D`

- Specify a [C]onfiguration command:

`babeld -C `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'redistribute metric 256'</span>

- Specify on which interfaces to operate:

`babeld `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wlan0</span>

---
layout: page
title: common/babeld (English)
description: "Routing daemon for Babel which uses firewall-style filters."
content_hash: 1e8818baeffaa363169ad00209e1742012f1b07f
last_modified_at: 2023-03-13
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># babeld

Routing daemon for Babel which uses firewall-style filters.
More information: <https://www.irif.fr/~jch/software/babel/babeld.html>.

- Start babeld with a specific configuration file:

`babeld -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/babeld.conf</span>

- Start babeld with multiple configuration files (read in order):

`babeld -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/ports.conf</span>` -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/filters.conf</span>` -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/interfaces.conf</span>

- Start babeld and daemonise afterwards:

`babeld -D`

- Start babeld and pass a configuration command:

`babeld -C `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'redistribute metric 256'</span>

- Start babeld and specify on which interfaces to operate:

`babeld `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wlan0</span>

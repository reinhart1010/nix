---
layout: page
title: linux/iptables-save (English)
description: "Save the `iptables` IPv4 configuration."
content_hash: ece0b41e50daab5b6515ff6fbf655bdca26c9749
last_modified_at: 2024-03-16
related_topics:
  - title: Nederlands version
    url: /nl/linux/iptables-save.html
    icon: bi bi-globe
tldri18n_status: 2
---
# iptables-save

Save the `iptables` IPv4 configuration.
Use `ip6tables-save` to do the same for IPv6.
More information: <https://manned.org/iptables-save>.

- Print the `iptables` configuration:

`sudo iptables-save`

- Print the `iptables` configuration of a specific [t]able:

`sudo iptables-save --table `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">table</span>

- Save the `iptables` configuration to a [f]ile:

`sudo iptables-save --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

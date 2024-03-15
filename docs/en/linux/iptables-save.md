---
layout: page
title: linux/iptables-save (English)
description: "Save the `iptables` IPv4 configuration."
content_hash: 45b70241e91087ddd4511c1d47fbb4e0dcf5255d
last_modified_at: 2024-03-15
related_topics:
  - title: Nederlands version
    url: /nl/linux/iptables-save.html
    icon: bi bi-globe
tldri18n_status: 2
---
# iptables-save

Save the `iptables` IPv4 configuration.
Use `ip6tables-save` to the same for IPv6.
More information: <https://manned.org/iptables-save>.

- Print the `iptables` configuration:

`sudo iptables-save`

- Print the `iptables` configuration of a specific [t]able:

`sudo iptables-save --table `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">table</span>

- Save the `iptables` configuration to a [f]ile:

`sudo iptables-save --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

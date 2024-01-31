---
layout: page
title: linux/networkctl (English)
description: "Query the status of network links."
content_hash: 4296a0a293dd02590b3471662d65ac1e10d3224d
last_modified_at: 2024-01-31
related_topics:
  - title: polski version
    url: /pl/linux/networkctl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# networkctl

Query the status of network links.
Manage the network configuration using `systemd-networkd`.
More information: <https://www.freedesktop.org/software/systemd/man/networkctl.html>.

- List existing links with their status:

`networkctl list`

- Show an overall network status:

`networkctl status`

- Bring network devices up:

`networkctl up `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface1 interface2 ...</span>

- Bring network devices down:

`networkctl down `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface1 interface2 ...</span>

- Renew dynamic configurations (e.g. IP addresses received from a DHCP server):

`networkctl renew `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface1 interface2 ...</span>

- Reload configuration files (.netdev and .network):

`networkctl reload`

- Reconfigure network interfaces (if you edited the config, you need to call `networkctl reload` first):

`networkctl reconfigure `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface1 interface2 ...</span>

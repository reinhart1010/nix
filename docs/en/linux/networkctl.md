---
layout: page
title: linux/networkctl (English)
description: "Query the status of network links."
content_hash: d9f7b088736aba6383256bb5a30eabfc364376df
last_modified_at: 2023-04-23
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># networkctl

Query the status of network links.
Manage the network configuration using `systemd-networkd`.
More information: <https://www.freedesktop.org/software/systemd/man/networkctl.html>.

- Show a list of existing links and their status:

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

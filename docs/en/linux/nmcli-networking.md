---
layout: page
title: linux/nmcli-networking (English)
description: "Manage the networking status of NetworkManager."
content_hash: 4383e21006d502006615cd54254445b1b2c69650
last_modified_at: 2023-11-12
related_topics:
  - title: Nederlands version
    url: /nl/linux/nmcli-networking.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nmcli networking

Manage the networking status of NetworkManager.
This subcommand can also be called with `nmcli n`.
More information: <https://networkmanager.dev/docs/api/latest/nmcli.html>.

- Show the networking status of NetworkManager:

`nmcli networking`

- Enable or disable networking and all interfaces managed by NetworkManager:

`nmcli networking `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">on|off</span>

- Show the last known connectivity state:

`nmcli networking connectivity`

- Show the current connectivity state:

`nmcli networking connectivity check`

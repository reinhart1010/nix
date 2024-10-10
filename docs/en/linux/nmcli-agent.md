---
layout: page
title: linux/nmcli-agent (English)
description: "Run `nmcli` as a NetworkManager secret agent or polkit agent."
content_hash: 6941ac766cc5f17b58f53a4d1f8a901686b860f2
last_modified_at: 2024-10-10
related_topics:
  - title: Nederlands version
    url: /nl/linux/nmcli-agent.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nmcli agent

Run `nmcli` as a NetworkManager secret agent or polkit agent.
This subcommand can also be called with `nmcli a`.
More information: <https://networkmanager.pages.freedesktop.org/NetworkManager/NetworkManager/nmcli.html>.

- Register `nmcli` as a secret agent and listen for secret requests:

`nmcli agent secret`

- Register `nmcli` as a polkit agent and listen for authorization requests:

`nmcli agent polkit`

- Register `nmcli` as a secret agent and a polkit agent:

`nmcli agent all`

---
layout: page
title: linux/nmcli-agent (English)
description: "Run nmcli as a NetworkManager secret agent or polkit agent."
content_hash: 887dc1c4d68f931565b915398db627acb1a9c1a9
---
# nmcli agent

Run nmcli as a NetworkManager secret agent or polkit agent.
This subcommand can also be called with `nmcli a`.
More information: <https://networkmanager.dev/docs/api/latest/nmcli.html>.

- Register nmcli as a secret agent and listen for secret requests:

`nmcli agent secret`

- Register nmcli as a polkit agent and listen for authorization requests:

`nmcli agent polkit`

- Register nmcli as a secret agent and a polkit agent:

`nmcli agent all`

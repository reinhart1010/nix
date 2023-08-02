---
layout: page
title: linux/nmcli-agent (English)
description: "Run `nmcli` as a NetworkManager secret agent or polkit agent."
content_hash: cda84b1b0af171c616ce7fab0ebb092988150c7a
last_modified_at: 2023-08-02
---
# nmcli agent

Run `nmcli` as a NetworkManager secret agent or polkit agent.
This subcommand can also be called with `nmcli a`.
More information: <https://networkmanager.dev/docs/api/latest/nmcli.html>.

- Register `nmcli` as a secret agent and listen for secret requests:

`nmcli agent secret`

- Register `nmcli` as a polkit agent and listen for authorization requests:

`nmcli agent polkit`

- Register `nmcli` as a secret agent and a polkit agent:

`nmcli agent all`

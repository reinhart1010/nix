---
layout: page
title: linux/nmcli-agent (English)
description: "Run nmcli as a NetworkManager secret agent or polkit agent."
content_hash: 73fcd560f8b767ff10791e0a742b0fb90dbf054a
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># nmcli agent

Run nmcli as a NetworkManager secret agent or polkit agent.
See also: `nmcli radio`.
More information: <https://networkmanager.dev/docs/api/latest/nmcli.html>.

- Register nmcli as a secret agent and listen for secret requests:

`nmcli agent secret`

- Register nmcli as a polkit agent and listen for authorization requests:

`nmcli agent polkit`

- Register nmcli as a secret agent and a polkit agent:

`nmcli agent all`

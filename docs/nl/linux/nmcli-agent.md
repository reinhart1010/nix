---
layout: page
title: linux/nmcli-agent (Nederlands)
description: "Draai `nmcli` als een NetworkManager secret/polkit agent."
content_hash: 7d76c6ec1e85e4008c5f166e5ef7988545506e28
last_modified_at: 2023-11-05
related_topics:
  - title: English version
    url: /en/linux/nmcli-agent.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># nmcli agent

Draai `nmcli` als een NetworkManager secret/polkit agent.
Dit subcommando kan ook aangeroepen worden met `nmcli a`.
Meer informatie: <https://networkmanager.dev/docs/api/latest/nmcli.html>.

- Registeer `nmcli` als een secret agent en luister naar geheime verzoeken:

`nmcli agent secret`

- Registreer `nmcli` als een polkit agent en luister naar authorizatie verzoeken:

`nmcli agent polkit`

- Registreer `nmcli` als een secret agent en als een polkit agent:

`nmcli agent all`

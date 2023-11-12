---
layout: page
title: linux/nmcli-agent (Nederlands)
description: "Draai `nmcli` als een NetworkManager secret/polkit agent."
content_hash: 7d76c6ec1e85e4008c5f166e5ef7988545506e28
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/nmcli-agent.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nmcli agent

Draai `nmcli` als een NetworkManager secret/polkit agent.
Dit subcommando kan ook aangeroepen worden met `nmcli a`.
Meer informatie: <https://networkmanager.dev/docs/api/latest/nmcli.html>.

- Registeer `nmcli` als een secret agent en luister naar geheime verzoeken:

`nmcli agent secret`

- Registreer `nmcli` als een polkit agent en luister naar authorizatie verzoeken:

`nmcli agent polkit`

- Registreer `nmcli` als een secret agent en als een polkit agent:

`nmcli agent all`

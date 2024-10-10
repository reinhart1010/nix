---
layout: page
title: linux/nmcli-agent (Nederlands)
description: "Draai `nmcli` als een NetworkManager secret/polkit agent."
content_hash: 22c48d94121d0fa79c975edff139e6074f188d75
last_modified_at: 2024-10-10
related_topics:
  - title: English version
    url: /en/linux/nmcli-agent.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nmcli agent

Draai `nmcli` als een NetworkManager secret/polkit agent.
Dit subcommando kan ook aangeroepen worden met `nmcli a`.
Meer informatie: <https://networkmanager.pages.freedesktop.org/NetworkManager/NetworkManager/nmcli.html>.

- Registeer `nmcli` als een secret agent en luister naar geheime verzoeken:

`nmcli agent secret`

- Registreer `nmcli` als een polkit agent en luister naar authorizatie verzoeken:

`nmcli agent polkit`

- Registreer `nmcli` als een secret agent en als een polkit agent:

`nmcli agent all`

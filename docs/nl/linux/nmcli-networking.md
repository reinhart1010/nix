---
layout: page
title: linux/nmcli-networking (Nederlands)
description: "Beheer de netwerk status of NetworkManager."
content_hash: aa0cf11848d3a19bb628007e044ba3dcb40cc829
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/nmcli-networking.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nmcli networking

Beheer de netwerk status of NetworkManager.
Dit subcommando kan ook aangeroepen worden met `nmcli n`.
Meer informatie: <https://networkmanager.dev/docs/api/latest/nmcli.html>.

- Toon de netwerk status of NetworkManager:

`nmcli networking`

- Schakel netwerk in/uit en alle interfaces die worden beheerd door NetworkManager:

`nmcli networking `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">on|off</span>

- Toon de laatst bekende connectiviteit status:

`nmcli networking connectivity`

- Toon de huidige connectiviteit status:

`nmcli networking connectivity check`

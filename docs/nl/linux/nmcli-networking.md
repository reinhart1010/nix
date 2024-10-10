---
layout: page
title: linux/nmcli-networking (Nederlands)
description: "Beheer de netwerk status of NetworkManager."
content_hash: 9c9117dde999c9c812821b6a230b49c675629419
last_modified_at: 2024-10-10
related_topics:
  - title: English version
    url: /en/linux/nmcli-networking.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nmcli networking

Beheer de netwerk status of NetworkManager.
Dit subcommando kan ook aangeroepen worden met `nmcli n`.
Meer informatie: <https://networkmanager.pages.freedesktop.org/NetworkManager/NetworkManager/nmcli.html>.

- Toon de netwerk status of NetworkManager:

`nmcli networking`

- Schakel netwerk in/uit en alle interfaces die worden beheerd door NetworkManager:

`nmcli networking `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">on|off</span>

- Toon de laatst bekende connectiviteit status:

`nmcli networking connectivity`

- Toon de huidige connectiviteit status:

`nmcli networking connectivity check`

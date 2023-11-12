---
layout: page
title: linux/nordvpn (English)
description: "Command-line interface for NordVPN."
content_hash: 3ca3a2c3cd5df1ab6ae8448559582d110d5a2392
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/linux/nordvpn.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nordvpn

Command-line interface for NordVPN.
More information: <https://nordvpn.com/download/linux/>.

- Interactively log into a NordVPN account:

`nordvpn login`

- Display the connection status:

`nordvpn status`

- Connect to the nearest NordVPN server:

`nordvpn connect`

- List all available countries:

`nordvpn countries`

- Connect to a NordVPN server in a specific country:

`nordvpn connect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Germany</span>

- Connect to a NordVPN server in a specific country and city:

`nordvpn connect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Germany</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Berlin</span>

- Set autoconnect option:

`nordvpn set autoconnect on`

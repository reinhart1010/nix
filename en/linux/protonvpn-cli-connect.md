---
layout: page
title: linux/protonvpn-cli-connect (English)
description: "Official client to connect to ProtonVPN from the command-line."
content_hash: 016d97cdad20edaebda96a340f34be87e3466ca2
---
# protonvpn-cli connect

Official client to connect to ProtonVPN from the command-line.
More information: <https://protonvpn.com/support/linux-vpn-setup/>.

- Connect to ProtonVPN interactively:

`protonvpn-cli connect`

- Connect to ProtonVPN using the fastest server available:

`protonvpn-cli connect --fastest`

- Connect to ProtonVPN using a specific server with a specific protocol:

`protonvpn-cli connect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">server_name</span>` --protocol `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">udp|tcp</span>

- Connect to ProtonVPN using a random server with a specific protocol:

`protonvpn-cli connect --random --protocol `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">udp|tcp</span>

- Connect to ProtonVPN using the fastest Tor-supporting server:

`protonvpn-cli connect --tor`

- Display help:

`protonvpn-cli connect --help`

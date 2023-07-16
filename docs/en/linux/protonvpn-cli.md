---
layout: page
title: linux/protonvpn-cli (English)
description: "Official ProtonVPN client."
content_hash: 6c983833b7d8224819d7dbbdd1de6aa9451d370f
last_modified_at: 2023-07-16
---
# protonvpn-cli

Official ProtonVPN client.
More information: <https://github.com/ProtonVPN/linux-cli>.

- Log in to the ProtonVPN account:

`protonvpn-cli login `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Start a kill switch upon connecting to ProtonVPN:

`protonvpn-cli killswitch --on`

- Connect to ProtonVPN interactively:

`protonvpn-cli connect`

- Display connection status:

`protonvpn-cli status`

- Block malware using ProtonVPN NetShield:

`protonvpn-cli netshield --malware`

- Disconnect from ProtonVPN:

`protonvpn-cli disconnect`

- Display the current ProtonVPN configuration:

`protonvpn-cli config --list`

- Display help for a subcommand:

`protonvpn-cli `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subcommand</span>` --help`

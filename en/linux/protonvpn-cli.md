---
layout: page
title: linux/protonvpn-cli (English)
description: "Official client for ProtonVPN service from the command-line."
content_hash: 3af01c46ab0ad4fcef452c5f9f4c34cc09dee51f
---
# protonvpn-cli

Official client for ProtonVPN service from the command-line.
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

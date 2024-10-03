---
layout: page
title: linux/protonvpn (English)
description: "Unofficial third-party ProtonVPN client."
content_hash: 8345d4038b8f045c6463732bc3983e81bff4ec11
last_modified_at: 2024-10-03
tldri18n_status: 2
---
# protonvpn

Unofficial third-party ProtonVPN client.
See also: `protonvpn-connect`.
More information: <https://github.com/Rafficer/linux-cli-community>.

- Initialize ProtonVPN profile:

`protonvpn init`

- Connect to ProtonVPN interactively:

`protonvpn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">c|connect</span>

- Display connection status:

`protonvpn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">s|status</span>

- Disconnect from ProtonVPN:

`protonvpn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">d|disconnect</span>

- Reconnect or connect to the last server used:

`protonvpn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">r|reconnect</span>

- Refresh OpenVPN configuration and server data:

`protonvpn refresh`

- Display help for a subcommand:

`protonvpn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subcommand</span>` --help`

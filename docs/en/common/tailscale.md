---
layout: page
title: common/tailscale (English)
description: "A private WireGuard network service."
content_hash: a262abcddf3b98c7445f93123f026da373c9b1f0
last_modified_at: 2024-10-05
tldri18n_status: 2
---
# tailscale

A private WireGuard network service.
Some subcommands such as `up` have their own usage documentation.
More information: <https://tailscale.com>.

- Connect to Tailscale:

`sudo tailscale up`

- Disconnect from Tailscale:

`sudo tailscale down`

- Display the current Tailscale IP addresses:

`tailscale ip`

- Ping a peer node at the Tailscale layer and display which route it took for each response:

`tailscale ping `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip|hostname</span>

- Analyze the local network conditions and display the result:

`tailscale netcheck`

- Start a web server for controlling Tailscale:

`tailscale web`

- Display a shareable identifier to help diagnose issues:

`tailscale bugreport`

- Display help for a subcommand:

`tailscale `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subcommand</span>` --help`

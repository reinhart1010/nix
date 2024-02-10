---
layout: page
title: common/tailscale-up (English)
description: "Connect the client to the Tailscale network."
content_hash: 8a40172ec5b910dec8df55756e29634e7aec9aa2
last_modified_at: 2024-02-10
tldri18n_status: 2
---
# tailscale up

Connect the client to the Tailscale network.
In version 1.8 and above, command-line arguments are stored and reused until they're overwritten or `--reset` is called.
More information: <https://tailscale.com/kb/1080/cli/#up>.

- Connect to Tailscale:

`sudo tailscale up`

- Connect and offer the current machine to be an exit node for internet traffic:

`sudo tailscale up --advertise-exit-node`

- Connect using a specific node for internet traffic:

`sudo tailscale up --exit-node=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">exit_node_ip</span>

- Connect and block incoming connections to the current node:

`sudo tailscale up --shields-up`

- Connect and don't accept DNS configuration from the admin panel (defaults to `true`):

`sudo tailscale up --accept-dns=false`

- Connect and configure Tailscale as a subnet router:

`sudo tailscale up --advertise-routes=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10.0.0.0/24,10.0.1.0/24,...</span>

- Connect and accept subnet routes from Tailscale:

`sudo tailscale up --accept-routes`

- Reset unspecified settings to their default values and connect:

`sudo tailscale up --reset`

---
layout: page
title: common/tailscale-up (English)
description: "Connects the client to the Tailscale network."
content_hash: 43dc5aa45bd03f8e7f8caf1ece4f5e305f13d274
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# tailscale up

Connects the client to the Tailscale network.
In version 1.8 and above, command-line arguments are stored and reused until they're overwritten or `--reset` is called.
More information: <https://tailscale.com/kb/admin/>.

- Connect to Tailscale:

`sudo tailscale up`

- Connect and offer the current machine to be an exit node for internet traffic:

`sudo tailscale up --advertise-exit-node`

- Connect using a specific node for internet traffic:

`sudo tailscale up --exit-node=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">exit_node_ip</span>

- Connect and block incoming connections to the current node:

`sudo tailscale up --shields-up`

- Connect and don't accept DNS configuration from the admin panel (defaults to `true`):

`sudo tailscale up --accept-dns=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">false</span>

- Connect and configure Tailscale as a subnet router:

`sudo tailscale up --advertise-routes=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10.0.0.0/24</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10.0.1.0/24</span>

- Connect and accept subnet routes from Tailscale:

`sudo tailscale up --accept-routes`

- Reset unspecified settings to their default values and connect:

`sudo tailscale up --reset`

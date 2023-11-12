---
layout: page
title: linux/f5fpc (English)
description: "A proprietary commercial SSL VPN client by BIG-IP Edge."
content_hash: 58fa7f3d106b3d1fb9544206dd041e260cbc9003
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# f5fpc

A proprietary commercial SSL VPN client by BIG-IP Edge.
More information: <https://techdocs.f5.com/kb/en-us/products/big-ip_apm/manuals/product/apm-client-configuration-11-4-0/4.html>.

- Open a new VPN connection:

`sudo f5fpc --start`

- Open a new VPN connection to a specific host:

`sudo f5fpc --start --host `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host.example.com</span>

- Specify a username (user will be prompted for a password):

`sudo f5fpc --start --host `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host.example.com</span>` --username `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user</span>

- Show the current VPN status:

`sudo f5fpc --info`

- Shutdown the VPN connection:

`sudo f5fpc --stop`

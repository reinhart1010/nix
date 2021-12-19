---
layout: page
title: linux/f5fpc (English)
description: "A proprietry commercial SSL VPN client by BIG-IP Edge."
content_hash: ff5ea6dab6f5fcff9b2b3c13fcaf268f4417bfe1
---
# f5fpc

A proprietry commercial SSL VPN client by BIG-IP Edge.
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

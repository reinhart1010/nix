---
layout: page
title: linux/lxc-network (English)
description: "Manage networks for LXD containers."
content_hash: 8f182635119b26eff0ccc676b2ac4fac92421504
---
# lxc network

Manage networks for LXD containers.
More information: <https://linuxcontainers.org/lxd/docs/master/networks>.

- List all available networks:

`lxc network list`

- Show the configuration of a specific network:

`lxc network show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">network_name</span>

- Add a running instance to a specific network:

`lxc network attach `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">network_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span>

- Create a new managed network:

`lxc network create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">network_name</span>

- Set a bridge interface of a specific network:

`lxc network set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">network_name</span>` bridge.external_interfaces `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>

- Disable NAT for a specific network:

`lxc network set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">network_name</span>` ipv`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>`.nat false`

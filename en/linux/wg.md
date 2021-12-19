---
layout: page
title: linux/wg (English)
description: "Manage the configuration of WireGuard interfaces."
content_hash: f3b31402ec769b2fc428f2eaf2c90f06ab87a1e4
related_topics:
  - title: français version
    url: /fr/linux/wg.html
    icon: bi bi-globe
---
# wg

Manage the configuration of WireGuard interfaces.
More information: <https://www.wireguard.com/quickstart/>.

- Check status of currently active interfaces:

`wg`

- Generate a new private key:

`wg genkey`

- Generate a public key from a private key:

`wg pubkey < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/private_key</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/public_key</span>

- Generate a public and private key:

`wg genkey | tee `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/private_key</span>` | wg pubkey > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/public_key</span>

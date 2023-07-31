---
layout: page
title: linux/wg (English)
description: "Manage the configuration of WireGuard interfaces."
content_hash: d265e8c557925d7b9515c0c725c18aab73336716
last_modified_at: 2023-07-31
related_topics:
  - title: français version
    url: /fr/linux/wg.html
    icon: bi bi-globe
---
# wg

Manage the configuration of WireGuard interfaces.
More information: <https://www.wireguard.com/quickstart/>.

- Check status of currently active interfaces:

`sudo wg`

- Generate a new private key:

`wg genkey`

- Generate a public key from a private key:

`wg pubkey < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/private_key</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/public_key</span>

- Generate a public and private key:

`wg genkey | tee `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/private_key</span>` | wg pubkey > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/public_key</span>

- Show the current configuration of a wireguard interface:

`sudo wg showconf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wg0</span>

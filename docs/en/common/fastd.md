---
layout: page
title: common/fastd (English)
description: "VPN daemon."
content_hash: 27fbcb45fd50d820833ae7cfed9030053630f9f8
last_modified_at: 2023-03-13
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># fastd

VPN daemon.
Works on Layer 2 or Layer 3, supports different encryption methods, used by Freifunk.
More information: <https://fastd.readthedocs.io/en/stable/>.

- Start fastd with a specific configuration file:

`fastd --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/fastd.conf</span>

- Start a Layer 3 VPN with an MTU of 1400, loading the rest of the configuration parameters from a file:

`fastd --mode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tap</span>` --mtu `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1400</span>` --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/fastd.conf</span>

- Validate a configuration file:

`fastd --verify-config --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/fastd.conf</span>

- Generate a new key:

`fastd --generate-key`

- Show the public key to a private key in a configuration file:

`fastd --show-key --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/fastd.conf</span>

- Show the current version::

`fastd -v`

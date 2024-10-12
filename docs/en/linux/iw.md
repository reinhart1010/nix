---
layout: page
title: linux/iw (English)
description: "Show and manipulate wireless devices."
content_hash: c8ebf19b4af0354e9d29a91a7e9ed5a23fb4841c
last_modified_at: 2024-10-12
tldri18n_status: 2
---
# iw

Show and manipulate wireless devices.
See also: `iw dev`.
More information: <https://wireless.docs.kernel.org/en/latest/en/users/documentation/iw.html>.

- Scan for available wireless networks:

`iw dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wlp</span>` scan`

- Join an open wireless network:

`iw dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wlp</span>` connect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">SSID</span>

- Close the current connection:

`iw dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wlp</span>` disconnect`

- Show information about the current connection:

`iw dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wlp</span>` link`

- List all physical and logical wireless network interfaces:

`iw dev`

- List all wireless capabilities for all physical hardware interfaces:

`iw phy`

- List the kernel's current wireless regulatory domain information:

`iw reg get`

- Display help for all commands:

`iw help`

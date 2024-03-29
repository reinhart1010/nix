---
layout: page
title: linux/iwlist (English)
description: "Get detailed information from a wireless interface."
content_hash: 0307eb30cf8dd68e2fc5df03b9441837d0a39505
last_modified_at: 2024-03-07
tldri18n_status: 2
---
# iwlist

Get detailed information from a wireless interface.
More information: <https://manned.org/iwlist.8>.

- Display the list of access points and ad-hoc cells in range:

`iwlist `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wireless_interface</span>` scan`

- Display available frequencies in the device:

`iwlist `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wireless_interface</span>` frequency`

- List the bit-rates supported by the device:

`iwlist `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wireless_interface</span>` rate`

- List the WPA authentication parameters currently set:

`iwlist `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wireless_interface</span>` auth`

- List all the WPA encryption keys set in the device:

`iwlist `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wireless_interface</span>` wpakeys`

- List the encryption key sizes supported and list all the encryption keys set in the device:

`iwlist `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wireless_interface</span>` keys`

- List the various power management attributes and modes of the device:

`iwlist `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wireless_interface</span>` power`

- List generic information elements set in the device (used for WPA support):

`iwlist `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wireless_interface</span>` genie`

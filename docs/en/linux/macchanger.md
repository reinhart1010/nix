---
layout: page
title: linux/macchanger (English)
description: "Command-line utility for manipulating network interface MAC addresses."
content_hash: ae61e3acc32f2429bb69a85b716d6cd03d9b10f0
last_modified_at: 2024-03-06
tldri18n_status: 2
---
# macchanger

Command-line utility for manipulating network interface MAC addresses.
More information: <https://manned.org/macchanger>.

- View the current and permanent MAC addresses of a interface:

`macchanger --show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface</span>

- Set interface to a random MAC:

`macchanger --random `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface</span>

- Set an interface to a random MAC address, and pretend to be a [b]urned-[i]n-[a]ddress:

`macchanger --random --bia `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface</span>

- Set an interface to a specific MAC address:

`macchanger --mac `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">XX:XX:XX:XX:XX:XX</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface</span>

- Print the identifications (the first three bytes of a MAC address) of all known vendors:

`macchanger --list`

- Reset an interface to its permanent hardware MAC address:

`macchanger --permanent `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface</span>

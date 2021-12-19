---
layout: page
title: linux/macchanger (English)
description: "Command-line utility for manipulating network interface MAC addresses."
content_hash: e2c5044c456bbf443bce655070df3c2bdfc10c2c
---
# macchanger

Command-line utility for manipulating network interface MAC addresses.
More information: <https://manned.org/macchanger>.

- View the current and permanent MAC addresses of a interface:

`macchanger --show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface</span>

- Set interface to a random MAC:

`macchanger --random `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface</span>

- Set interface to a specific MAC:

`macchanger --mac `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">XX:XX:XX:XX:XX:XX</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface</span>

- Reset interface to its permanent hardware MAC:

`macchanger --permanent `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface</span>

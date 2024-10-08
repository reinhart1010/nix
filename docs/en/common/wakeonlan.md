---
layout: page
title: common/wakeonlan (English)
description: "Send packets to wake-on-LAN (WOL) enabled PCs."
content_hash: 655f345a292e56a60b10f821d05b4af1f0c8a780
last_modified_at: 2024-08-11
tldri18n_status: 2
---
# wakeonlan

Send packets to wake-on-LAN (WOL) enabled PCs.
More information: <https://github.com/jpoliv/wakeonlan>.

- Send packets to all devices on the local network (255.255.255.255) by specifying a MAC address:

`wakeonlan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">01:02:03:04:05:06</span>

- Send packet to a specific device via IP address:

`wakeonlan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">01:02:03:04:05:06</span>` -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.178.2</span>

- Print the commands, but don't execute them (dry-run):

`wakeonlan -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">01:02:03:04:05:06</span>

- Run in quiet mode:

`wakeonlan -q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">01:02:03:04:05:06</span>

---
layout: page
title: linux/nmcli-radio (English)
description: "Show the status of radio switches or enable/disable them using NetworkManager."
content_hash: cc86286bd4a4b8d015bde316942cd3a64cf5a9a7
last_modified_at: 2024-10-10
related_topics:
  - title: Nederlands version
    url: /nl/linux/nmcli-radio.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nmcli radio

Show the status of radio switches or enable/disable them using NetworkManager.
This subcommand can also be called with `nmcli r`.
More information: <https://networkmanager.pages.freedesktop.org/NetworkManager/NetworkManager/nmcli.html>.

- Show status of Wi-Fi:

`nmcli radio wifi`

- Turn Wi-Fi on or off:

`nmcli radio wifi `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">on|off</span>

- Show status of WWAN:

`nmcli radio wwan`

- Turn WWAN on or off:

`nmcli radio wwan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">on|off</span>

- Show status of both switches:

`nmcli radio all`

- Turn both switches on or off:

`nmcli radio all `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">on|off</span>

---
layout: page
title: linux/nmcli-radio (English)
description: "Show radio switches status or enable and disable switches."
content_hash: cb0a33a125e480b06c645d518e4a81c8c03b6ade
---
# nmcli radio

Show radio switches status or enable and disable switches.
This subcommand can also be called with `nmcli r`.
More information: <https://networkmanager.dev/docs/api/latest/nmcli.html>.

- Show status of Wi-Fi in NetworkManager:

`nmcli radio wifi`

- Turn Wi-Fi on or off in NetworkManager:

`nmcli radio wifi `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">on|off</span>

- Show status of WWAN in NetworkManager:

`nmcli radio wwan`

- Turn WWAN on or off in NetworkManager:

`nmcli radio wwan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">on|off</span>

- Show status of both switches in NetworkManager:

`nmcli radio all`

- Turn both switches on or off in NetworkManager:

`nmcli radio all `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">on|off</span>

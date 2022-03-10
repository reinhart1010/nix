---
layout: page
title: linux/nmcli-radio (English)
description: "Show radio switches status or enable and disable switches."
content_hash: 80964c229cc4ed49628590899efd709d384b96f0
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># nmcli radio

Show radio switches status or enable and disable switches.
See also: `nmcli agent`.
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

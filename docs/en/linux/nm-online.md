---
layout: page
title: linux/nm-online (English)
description: "Ask NetworkManager whether the network is connected."
content_hash: 0a83ecc01a0fcff00e841b37122543a7fcdc058f
last_modified_at: 2023-08-09
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># nm-online

Ask NetworkManager whether the network is connected.
More information: <https://networkmanager.dev/docs/api/latest/nm-online.html>.

- Find out whether the network is connected and print the result to `stdout`:

`nm-online`

- Wait `n` seconds for a connection (30 by default):

`nm-online --timeout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>

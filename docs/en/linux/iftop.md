---
layout: page
title: linux/iftop (English)
description: "Show bandwidth usage on an interface by host."
content_hash: 26e60396ceed0eb281668a21159a7fa921cb119f
last_modified_at: 2024-01-30
tldri18n_status: 2
---
# iftop

Show bandwidth usage on an interface by host.
More information: <https://manned.org/iftop>.

- Show the bandwidth usage:

`sudo iftop`

- Show the bandwidth usage of a given interface:

`sudo iftop -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface</span>

- Show the bandwidth usage with port information:

`sudo iftop -P`

- Do not show bar graphs of traffic:

`sudo iftop -b`

- Do not look up hostnames:

`sudo iftop -n`

- Display help:

`?`

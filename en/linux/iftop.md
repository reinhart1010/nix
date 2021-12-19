---
layout: page
title: linux/iftop (English)
description: "Show bandwidth usage on an interface by host."
content_hash: 17210abd396353ecb50c459568e39ad8f37cfdd3
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

- Get help about interactive commands:

`?`

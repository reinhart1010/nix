---
layout: page
title: common/trawl (English)
description: "Prints out network interface information to the console, much like ifconfig/ipconfig/ip/ifdata."
content_hash: ffb521d4775620638e02996b7102d40e1a50980f
last_modified_at: 2024-01-31
tldri18n_status: 2
---
# trawl

Prints out network interface information to the console, much like ifconfig/ipconfig/ip/ifdata.
More information: <https://github.com/robphoenix/trawl>.

- Show column names:

`trawl -n`

- Filter interface names using a case-insensitive regular expression:

`trawl -f wi`

- List available interfaces:

`trawl -i`

- Include the loopback interface:

`trawl -l`

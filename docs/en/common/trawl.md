---
layout: page
title: common/trawl (English)
description: "Prints out network interface information to the console, much like ifconfig/ipconfig/ip/ifdata."
content_hash: e1679ef38b77b19e0d58770e2ebe60278a917f9f
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# trawl

Prints out network interface information to the console, much like ifconfig/ipconfig/ip/ifdata.
More information: <https://github.com/robphoenix/trawl>.

- Show column names:

`trawl -n`

- Filter interface names using a case-insensitive regular expression:

`trawl -f wi`

- Get a list of available interfaces:

`trawl -i`

- Include the loopback interface:

`trawl -l`

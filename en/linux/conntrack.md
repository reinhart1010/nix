---
layout: page
title: linux/conntrack (English)
description: "Interact with the Netfilter connection tracking system."
content_hash: fa5f77a821f9725fe7e6fc290d3c42412b83d05b
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># conntrack

Interact with the Netfilter connection tracking system.
Search, list, inspect, modify, and delete connection flows.
More information: <https://manned.org/conntrack>.

- List all currently tracked connections:

`conntrack --dump`

- Display a real-time event log of connection changes:

`conntrack --event`

- Display a real-time event log of connection changes and associated timestamps:

`conntrack --event -o timestamp`

- Display a real-time event log of connection changes for a specific IP address:

`conntrack --event --orig-src `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_address</span>

- Delete all flows for a specific source IP address:

`conntrack --delete --orig-src `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_address</span>

---
layout: page
title: linux/iptables-restore (English)
description: "Restore the `iptables` IPv4 configuration."
content_hash: 1907e409314e01ff35bb1f58c0bedd34ab3c6b15
last_modified_at: 2023-09-18
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># iptables-restore

Restore the `iptables` IPv4 configuration.
Use `ip6tables-restore` to do the same for IPv6.
More information: <https://manned.org/iptables-restore>.

- Restore the `iptables` configuration from a file:

`sudo iptables-restore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

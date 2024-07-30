---
layout: page
title: osx/netstat (English)
description: "Display network-related information such as open connections, open socket ports, etc."
content_hash: c13545b9b1cc9b54e6b51a31b8b9be2d0cd1741d
last_modified_at: 2024-07-30
tldri18n_status: 2
---
# netstat

Display network-related information such as open connections, open socket ports, etc.
See also: `lsof` for listing network connections, including listening ports.
More information: <https://keith.github.io/xcode-man-pages/netstat.1.html>.

- Display the PID and program name listening on a specific protocol:

`netstat -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">protocol</span>

- Print the routing table and do not resolve IP addresses to hostnames:

`netstat -nr`

- Print the routing table of IPv4 addresses:

`netstat -nr -f inet`

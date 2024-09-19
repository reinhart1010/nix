---
layout: page
title: netbsd/sockstat (English)
description: "List open Internet or UNIX domain sockets."
content_hash: 2ec0ecc772e20360e2af6e9f41b53cd384be8b7c
last_modified_at: 2024-09-19
related_topics:
  - title: español version
    url: /es/netbsd/sockstat.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/netbsd/sockstat.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/netbsd/sockstat.html
    icon: bi bi-globe
tldri18n_status: 2
---
# sockstat

List open Internet or UNIX domain sockets.
Note: this program is a rewrite for NetBSD 3.0 from FreeBSD's `sockstat`.
See also: `netstat`.
More information: <https://man.netbsd.org/sockstat.1>.

- Show information for IPv4, IPv6 and Unix sockets for both listening and connected sockets:

`sockstat`

- Show information for IPv[4]/IPv[6] sockets [l]istening on specific [p]orts using a specific [P]rotocol:

`sockstat -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4|6</span>` -l -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tcp|udp|sctp|divert</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port1,port2...</span>

- Also show [c]onnected sockets, showing [u]nix sockets:

`sockstat -cu`

- Only show [n]umeric output, without resolving symbolic names for addresses and ports:

`sockstat -n`

- Only list sockets of the specified address [f]amily:

`sockstat -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">inet|inet6|local|unix</span>

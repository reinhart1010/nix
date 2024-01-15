---
layout: page
title: netbsd/sockstat (English)
description: "List open Internet or UNIX domain sockets."
content_hash: 85547ae0e7d09ff0ead91fcb916393b31ad5bd64
last_modified_at: 2024-01-15
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/netbsd/sockstat.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># sockstat

List open Internet or UNIX domain sockets.
Note: this program is a rewrite for NetBSD 3.0 from FreeBSD's `sockstat`.
See also: `netstat`.
More information: <https://man.freebsd.org/cgi/man.cgi?sockstat>.

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

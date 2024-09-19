---
layout: page
title: netbsd/sockstat (Nederlands)
description: "Toon open Internet- of UNIX-domeinsockets."
content_hash: f34daff4c142c948138599be4ea45481d2fdd35a
last_modified_at: 2024-09-19
related_topics:
  - title: English version
    url: /en/netbsd/sockstat.html
    icon: bi bi-globe
  - title: español version
    url: /es/netbsd/sockstat.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/netbsd/sockstat.html
    icon: bi bi-globe
tldri18n_status: 2
---
# sockstat

Toon open Internet- of UNIX-domeinsockets.
Let op: dit programma is hergeschreven voor NetBSD 3.0 van FreeBSD's `sockstat`.
Bekijk ook: `netstat`.
Meer informatie: <https://man.netbsd.org/sockstat.1>.

- Toon informatie voor IPv4- en IPv6-sockets voor zowel luister- als verbonden sockets:

`sockstat`

- Toon informatie voor IPv[4]/IPv[6] sockets die [l]uisteren op specifieke [p]oorten met een specifiek [P]rotocol:

`sockstat -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4|6</span>` -l -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tcp|udp|sctp|divert</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port1,port2...</span>

- Toon ook [c]onnected sockets en [u]nix-sockets:

`sockstat -cu`

- Toon alleen [n]umerieke output, zonder symbolische namen voor adressen en poorten te resolven:

`sockstat -n`

- Toon alleen sockets van de opgegeven adres[f]amilie:

`sockstat -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">inet|inet6|local|unix</span>

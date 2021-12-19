---
layout: page
title: linux/ss (English)
description: "Utility to investigate sockets."
content_hash: 4595a7c996baf0a851ca3a9f64772e1da1d3e37d
---
# ss

Utility to investigate sockets.
More information: <https://manned.org/ss.8>.

- Show all TCP/UDP/RAW/UNIX sockets:

`ss -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-t|-u|-w|-x</span>

- Filter TCP sockets by states, only/exclude:

`ss `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">state/exclude</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bucket/big/connected/synchronized/...</span>

- Show all TCP sockets connected to the local HTTPS port (443):

`ss -t src :`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">443</span>

- Show all TCP sockets listening on the local 8080 port:

`ss -lt src :`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8080</span>

- Show all TCP sockets along with processes connected to a remote ssh port:

`ss -pt dst :`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ssh</span>

- Show all UDP sockets connected on specific source and destination ports:

`ss -u 'sport == :`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source_port</span>` and dport == :`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">destination_port</span>`'`

- Show all TCP IPv4 sockets locally connected on the subnet 192.168.0.0/16:

`ss -4t src `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168/16</span>

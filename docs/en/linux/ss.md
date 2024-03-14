---
layout: page
title: linux/ss (English)
description: "Utility to investigate sockets."
content_hash: a633913a6a826c736b552601606372f91a15f3f8
last_modified_at: 2024-03-14
tldri18n_status: 2
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

- Show all TCP sockets along with processes connected to a remote SSH port:

`ss -pt dst :`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ssh</span>

- Show all UDP sockets connected on specific source and destination ports:

`ss -u 'sport == :`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source_port</span>` and dport == :`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">destination_port</span>`'`

- Show all TCP IPv4 sockets locally connected on the subnet 192.168.0.0/16:

`ss -4t src `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168/16</span>

- Kill IPv4 or IPv6 Socket Connection with destination IP 192.168.1.17 and destination port 8080:

`ss --kill dst `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.1.17</span>` dport = `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8080</span>

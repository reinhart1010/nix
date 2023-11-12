---
layout: page
title: common/bandwhich (English)
description: "Display the current network utilization by process, connection or remote IP/hostname."
content_hash: 68deb037b5cc9704bb06657f9fbf56bb6a192010
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# bandwhich

Display the current network utilization by process, connection or remote IP/hostname.
More information: <https://github.com/imsnif/bandwhich>.

- Show the remote addresses table only:

`bandwhich --addresses`

- Show DNS queries:

`bandwhich --show-dns`

- Show total (cumulative) usage:

`bandwhich --total-utilization`

- Show the network utilization for a specific network interface:

`bandwhich --interface `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>

- Show DNS queries with a given DNS server:

`bandwhich --show-dns --dns-server `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dns_server_ip</span>

---
layout: page
title: common/ipsumdump (English)
description: "Summarise TCP/IP dumps into a human and machine readable ASCII format."
content_hash: 7448666177be053b9eb34699124d14f981cba858
last_modified_at: 2024-03-14
tldri18n_status: 2
---
# ipsumdump

Summarise TCP/IP dumps into a human and machine readable ASCII format.
More information: <https://manned.org/ipsumdump>.

- Print the source and destination IP addresses of all packets in a PCAP file:

`ipsumdump --src --dst `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.pcap</span>

- Print the timestamps, source address, source port, destination address, destination port and protocol of all packets read from a given network interface:

`ipsumdump --interface `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>` -tsSdDp`

- Print the anonymised source address, anonymised destination address, and IP packet length of all packets in a PCAP file:

`ipsumdump --src --dst --length --anonymize `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.pcap</span>

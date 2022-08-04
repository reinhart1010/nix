---
layout: page
title: common/tcpdump (English)
description: "Dump traffic on a network."
content_hash: 75f0e9b528935fd51ee9484df26d0bd1deef0daf
---
# tcpdump

Dump traffic on a network.
More information: <https://www.tcpdump.org>.

- List available network interfaces:

`tcpdump -D`

- Capture the traffic of a specific interface:

`tcpdump -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>

- Capture all TCP traffic showing contents (ASCII) in console:

`tcpdump -A tcp`

- Capture the traffic from or to a host:

`tcpdump host `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">www.example.com</span>

- Capture the traffic from a specific interface, source, destination and destination port:

`tcpdump -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>` src `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.1.1</span>` and dst `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.1.2</span>` and dst port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">80</span>

- Capture the traffic of a network:

`tcpdump net `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.1.0/24</span>

- Capture all traffic except traffic over port 22 and save to a dump file:

`tcpdump -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dumpfile.pcap</span>` port not `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">22</span>

- Read from a given dump file:

`tcpdump -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dumpfile.pcap</span>

---
layout: page
title: common/scamper (English)
description: "Actively probes the Internet in order to analyze topology and performance."
content_hash: d31cfe053b232f6839f374fdc6bfc431776a2424
last_modified_at: 2024-11-09
related_topics:
  - title: Deutsch version
    url: /de/common/scamper.html
    icon: bi bi-globe
tldri18n_status: 2
---
# scamper

Actively probes the Internet in order to analyze topology and performance.
Includes some tools that start with `sc_`, for example `sc_warts2text` or `sc_ttlexp`.
More information: <https://www.caida.org/catalog/software/scamper/>.

- Execute the standard option (traceroute) to a destination:

`scamper -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.0.2.1</span>

- Execute two actions (ping and traceroute) on two different targets:

`scamper -I "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ping</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.0.2.1</span>`" -I "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">trace</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.0.2.2</span>`"`

- Ping several hosts with UDP, use a specific port number for the first ping and increase it for each subsequent ping:

`scamper -c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ping</span>` -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">UDP-dport</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">33434</span>`" -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.0.2.1</span>` -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.0.2.2</span>

- Use the Multipath Discovery Algorithm (MDA) to determine the presence of load-balanced paths to the destination and use ICMP echo packets to sample with a maximum of three attempts, write the result to a `warts` file:

`scamper -O `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">warts</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.warts</span>` -I "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tracelb</span>` -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ICMP-echo</span>` -q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.0.2.1</span>`"`

- Execute a Paris traceroute with ICMP to a destination and save the result in a compressed `warts` file:

`scamper -O `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">warts.gz</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.warts</span>` -I "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">trace</span>` -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">icmp-paris</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2001:db8:dead:beaf::4</span>`"`

- Record all ICMP packets that arrive at a specific IP address and have a specific ICMP ID in a `warts` file:

`scamper -O `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">warts</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.warts</span>` -I "sniff -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2001:db8:dead:beef::6</span>` icmp[icmpid] == `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">101</span>`"`

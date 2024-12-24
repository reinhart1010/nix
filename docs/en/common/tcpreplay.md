---
layout: page
title: common/tcpreplay (English)
description: "Replay network traffic stored in a `pcap` file."
content_hash: 6b571e0fda0bd24e01a370ed0ed1f9ead8a728ac
last_modified_at: 2024-12-24
tldri18n_status: 2
---
# tcpreplay

Replay network traffic stored in a `pcap` file.
More information: <https://tcpreplay.appneta.com/>.

- List available network interfaces:

`tcpreplay --listnics`

- Replay traffic to interface:

`tcpreplay -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">traffic.pcap</span>

- Replay traffic to interface and `stdout`:

`tcpreplay -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>` --verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">traffic.pcap</span>

- Replay traffic to interface as fast as possible:

`tcpreplay -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>` --topspeed `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">traffic.pcap</span>

- Replay traffic to interface at given Mbps:

`tcpreplay -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>` -M `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">traffic.pcap</span>

- Replay traffic to interface several times:

`tcpreplay -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>` --loop=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">num_times</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">traffic.pcap</span>

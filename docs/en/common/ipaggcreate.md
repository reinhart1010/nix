---
layout: page
title: common/ipaggcreate (English)
description: "Produce aggregate statistics of TCP/IP dumps."
content_hash: bbb8267d0ee714cf104c387cb5b62a95a1de565e
last_modified_at: 2024-03-14
tldri18n_status: 2
---
# ipaggcreate

Produce aggregate statistics of TCP/IP dumps.
More information: <https://manned.org/ipaggcreate>.

- Count the number of packets sent from each source address appearing in a PCAP file:

`ipaggcreate --src `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.pcap</span>

- Group and count packets read from a network interface by IP packet length:

`ipaggcreate --interface `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>` --length`

- Count the number of bytes sent between each address pair appearing in a PCAP file:

`ipaggcreate --address-pairs --bytes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.pcap</span>

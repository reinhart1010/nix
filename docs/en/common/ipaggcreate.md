---
layout: page
title: common/ipaggcreate (English)
description: "Produce aggregate statistics of TCP/IP dumps."
content_hash: 00410e7e75e2b1bdcc3289d537d9b7b7627f67df
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# ipaggcreate

Produce aggregate statistics of TCP/IP dumps.
More information: <https://manned.org/ipaggcreate>.

- Count the number of packets sent from each source address appearing in a pcap file:

`ipaggcreate --src `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.pcap</span>

- Group and count packets read from a network interface by IP packet length:

`ipaggcreate --interface `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>` --length`

- Count the number of bytes sent between each address pair appearing in a pcap file:

`ipaggcreate --address-pairs --bytes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.pcap</span>

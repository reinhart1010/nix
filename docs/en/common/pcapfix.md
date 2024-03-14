---
layout: page
title: common/pcapfix (English)
description: "Repair damaged or corrupted PCAP and PcapNG files."
content_hash: 65c999d049516ef96d0d49d90d71ed92b63dc837
last_modified_at: 2024-03-14
related_topics:
  - title: español version
    url: /es/common/pcapfix.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pcapfix

Repair damaged or corrupted PCAP and PcapNG files.
More information: <https://f00l.de/pcapfix/>.

- Repair a PCAP/PCapNG file (Note: for PCAP files, only the first 262144 bytes of each packet are scanned):

`pcapfix `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.pcapng</span>

- Repair an entire PCAP file:

`pcapfix --deep-scan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.pcap</span>

- Repair a PCAP/PcapNG file and write the repaired file to the specified location:

`pcapfix --outfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/repaired.pcap</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.pcap</span>

- Repair a PcapNG file and treat it as a PcapNG file, ignoring the automatic recognition:

`pcapfix --pcapng `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.pcapng</span>

- Repair a file and show the process in detail:

`pcapfix --verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.pcap</span>

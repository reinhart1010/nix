---
layout: page
title: common/pcapfix (English)
description: "Repair damaged or corrupted `pcap` and `pcapng` files."
content_hash: ea1d5ba4471badd75ec7f6ed8220a4fa51f39eab
last_modified_at: 2024-02-14
tldri18n_status: 2
---
# pcapfix

Repair damaged or corrupted `pcap` and `pcapng` files.
More information: <https://f00l.de/pcapfix/>.

- Repair a `pcap`/`pcapng` file (Note: for `pcap` files, only the first 262144 bytes of each packet are scanned):

`pcapfix `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.pcapng</span>

- Repair an entire `pcap` file:

`pcapfix --deep-scan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.pcap</span>

- Repair a `pcap`/`pcapng` file and write the repaired file to the specified location:

`pcapfix --outfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/repaired.pcap</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.pcap</span>

- Repair a `pcapng` file and treat it as a `pcapng` file, ignoring the automatic recognition:

`pcapfix --pcapng `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.pcapng</span>

- Repair a file and show the process in detail:

`pcapfix --verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.pcap</span>

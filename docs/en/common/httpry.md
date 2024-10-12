---
layout: page
title: common/httpry (English)
description: "A lightweight packet sniffer for displaying and logging HTTP traffic."
content_hash: 77328d6a7e3a38848b5c01e217b71b7980575746
last_modified_at: 2024-10-12
tldri18n_status: 2
---
# httpry

A lightweight packet sniffer for displaying and logging HTTP traffic.
It can be run in real-time displaying the traffic as it is parsed, or as a daemon process that logs to an output file.
More information: <https://dumpsterventures.com/jason/httpry/>.

- Save output to a file:

`httpry -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.log</span>

- Listen on a specific interface and save output to a binary PCAP format file:

`httpry `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>` -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.pcap</span>

- Filter output by a comma-separated list of HTTP verbs:

`httpry -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">get|post|put|head|options|delete|trace|connect|patch</span>

- Read from an input capture file and filter by IP:

`httpry -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.log</span>` '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host 192.168.5.25</span>`'`

- Run as daemon process:

`httpry -d -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.log</span>

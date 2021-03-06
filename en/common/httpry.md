---
layout: page
title: common/httpry (English)
description: "A lightweight packet sniffer for displaying and logging HTTP traffic."
content_hash: 1044d0ab8d21b5995d6e3e759df36ee3a13594be
---
# httpry

A lightweight packet sniffer for displaying and logging HTTP traffic.
It can be run in real-time displaying the traffic as it is parsed, or as a daemon process that logs to an output file.
More information: <http://dumpsterventures.com/jason/httpry/>.

- Save output to a file:

`httpry -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.log</span>

- Listen on a specific interface and save output to a binary pcap format file:

`httpry `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>` -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.pcap</span>

- Filter output by a comma-separated list of HTTP verbs:

`httpry -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">get|post|put|head|options|delete|trace|connect|patch</span>

- Read from an input capture file and filter by IP:

`httpry -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.log</span>` '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host 192.168.5.25</span>`'`

- Run as daemon process:

`httpry -d -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.log</span>

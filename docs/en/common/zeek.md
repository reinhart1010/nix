---
layout: page
title: common/zeek (English)
description: "Passive network traffic analyzer."
content_hash: 46e7d7de315618310d40ac2800a8903787c8e29d
---
# zeek

Passive network traffic analyzer.
Any output and log files will be saved to the current working directory.
More information: <https://docs.zeek.org/en/lts/quickstart.html#zeek-as-a-command-line-utility>.

- Analyze live traffic from a network interface:

`sudo zeek --iface `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface</span>

- Analyze live traffic from a network interface and load custom scripts:

`sudo zeek --iface `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">script1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">script2</span>

- Analyze live traffic from a network interface, without loading any scripts:

`sudo zeek --bare-mode --iface `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface</span>

- Analyze live traffic from a network interface, applying a `tcpdump` filter:

`sudo zeek --filter `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/filter</span>` --iface `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface</span>

- Analyze live traffic from a network interface using a watchdog timer:

`sudo zeek --watchdog --iface `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface</span>

- Analyze traffic from a `pcap` file:

`zeek --readfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.trace</span>

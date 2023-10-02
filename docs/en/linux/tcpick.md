---
layout: page
title: linux/tcpick (English)
description: "Packet sniffing and network traffic analysis tool."
content_hash: de0f1737badf56d9c1773b1e066e51d754c5ae68
last_modified_at: 2023-10-02
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># tcpick

Packet sniffing and network traffic analysis tool.
It can capture and display TCP connections and data. It can also monitor network traffic on a specific interface, host, or port.
More information: <https://manned.org/tcpick.8>.

- Capture traffic on a specific [i]nterface, port and host::

`sudo tcpick -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface</span>` -C -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>

- Capture traffic on port 80 (HTTP) of a specific host:

`sudo tcpick -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>` -C -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.1.100</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">80</span>

- Display help:

`tcpick --help`

---
layout: page
title: common/dumpcap (English)
description: "A network traffic dump tool."
content_hash: c265362074a9d1591ff5abe071a442b2c6ab09db
---
# dumpcap

A network traffic dump tool.
More information: <https://www.wireshark.org/docs/man-pages/dumpcap.html>.

- Display available interfaces:

`dumpcap --list-interfaces`

- Capture packets on a specific interface:

`dumpcap --interface `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>

- Capture packets to a specific location:

`dumpcap --interface `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file.pcapng</span>

- Write to a ring buffer with a specific max file limit of a specific size:

`dumpcap --interface `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file.pcapng</span>` --ring-buffer filesize:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">500000</span>` --ring-buffer files:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>

---
layout: page
title: common/sngrep (English)
description: "Display SIP calls message flows from terminal."
content_hash: 38613af68d3bfed6ba85bae004e092cc073fb2b6
last_modified_at: 2024-02-15
tldri18n_status: 2
---
# sngrep

Display SIP calls message flows from terminal.
More information: <https://github.com/irontec/sngrep>.

- Visualize SIP packets from a PCAP file:

`sngrep -I `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.pcap</span>

- Visualize only dialogs starting with INVITE packets with RTP packets from a PCAP file:

`sngrep -crI `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.pcap</span>

- Real-time interface with only dialogs starting with INVITE packets with RTP packets:

`sngrep -cr`

- Only capture packets without interface to a file:

`sngrep -NO `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.pcap</span>

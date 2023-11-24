---
layout: page
title: common/sngrep (English)
description: "Tool for displaying SIP calls message flows from terminal."
content_hash: 0977ffc763ce83d8e9f648e4ddbfdf73cb2b37f9
last_modified_at: 2023-11-24
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/sngrep.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># sngrep

Tool for displaying SIP calls message flows from terminal.
More information: <https://github.com/irontec/sngrep>.

- Visualize SIP packets from a PCAP file:

`sngrep -I `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.pcap</span>

- Visualize only dialogs starting with INVITE packets with RTP packets from a PCAP file:

`sngrep -crI `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.pcap</span>

- Real-time interface with only dialogs starting with INVITE packets with RTP packets:

`sngrep -cr`

- Only capture packets without interface to a file:

`sngrep -NO `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.pcap</span>

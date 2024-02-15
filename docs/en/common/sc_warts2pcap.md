---
layout: page
title: common/sc_warts2pcap (English)
description: "Write packets included in `warts` object to a `pcap` file."
content_hash: afba3bf849b8f0470cb5d6ab034859effc3d152a
last_modified_at: 2024-02-15
tldri18n_status: 2
---
# sc_warts2pcap

Write packets included in `warts` object to a `pcap` file.
This is only possible for tbit, sting and sniff.
More information: <https://www.caida.org/catalog/software/scamper/>.

- Convert the data from several `warts` files into one `pcap` file:

`sc_warts2pcap -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pcap</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1.warts path/to/file2.warts ...</span>

- Convert the data from a `warts` file into a `pcap` file and sort the packets by timestamp:

`sc_warts2pcap -s -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pcap</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.warts</span>

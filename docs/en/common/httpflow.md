---
layout: page
title: common/httpflow (English)
description: "A command-line utility to capture and dump HTTP streams."
content_hash: 2325b19b881fe9927bca16a35393f7b195e5b849
last_modified_at: 2024-03-14
tldri18n_status: 2
---
# httpflow

A command-line utility to capture and dump HTTP streams.
More information: <https://github.com/six-ddc/httpflow>.

- Capture traffic on all interfaces:

`httpflow -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">any</span>

- Use a bpf-style capture to filter the results:

`httpflow `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host httpbin.org or host baidu.com</span>

- Use a regular expression to filter requests by URLs:

`httpflow -u '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regular_expression</span>`'`

- Read packets from PCAP format binary file:

`httpflow -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">out.cap</span>

- Write the output to a directory:

`httpflow -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

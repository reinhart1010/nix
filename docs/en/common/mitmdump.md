---
layout: page
title: common/mitmdump (English)
description: "View, record, and programmatically transform HTTP traffic."
content_hash: 05fe4879ee55eb1827a74368aca8ea053a2a9f3c
last_modified_at: 2023-11-20
tldri18n_status: 2
---
# mitmdump

View, record, and programmatically transform HTTP traffic.
The command-line counterpart to mitmproxy.
More information: <https://docs.mitmproxy.org/stable/#mitmdump>.

- Start a proxy and save all output to a file:

`mitmdump -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Filter a saved traffic file to just POST requests:

`mitmdump -nr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input_filename</span>` -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output_filename</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">~m post</span>`"`

- Replay a saved traffic file:

`mitmdump -nc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

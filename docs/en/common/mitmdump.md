---
layout: page
title: common/mitmdump (English)
description: "View, record, and programmatically transform HTTP traffic."
content_hash: 6d4fb36a80780e919ea7c4ff5c43adf783930e0e
last_modified_at: 2022-12-06
---
# mitmdump

View, record, and programmatically transform HTTP traffic.
The command-line counterpart to mitmproxy.
More information: <https://docs.mitmproxy.org/stable/overview-tools/#mitmdump>.

- Start a proxy and save all output to a file:

`mitmdump -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Filter a saved traffic file to just POST requests:

`mitmdump -nr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input_filename</span>` -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output_filename</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">~m post</span>`"`

- Replay a saved traffic file:

`mitmdump -nc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

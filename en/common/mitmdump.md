---
layout: page
title: common/mitmdump (English)
description: "View, record, and programmatically transform HTTP traffic."
content_hash: 96976b454271cf87b48e710824327ce3d26176c6
---
# mitmdump

View, record, and programmatically transform HTTP traffic.
The command-line counterpart to mitmproxy.
More information: <https://docs.mitmproxy.org/stable/overview-tools/#mitmdump>.

- Start a proxy and save all output to a file:

`mitmdump -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>

- Filter a saved traffic file to just POST requests:

`mitmdump -nr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input_filename</span>` -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output_filename</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">~m post</span>`"`

- Replay a saved traffic file:

`mitmdump -nc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>

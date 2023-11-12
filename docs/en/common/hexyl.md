---
layout: page
title: common/hexyl (English)
description: "A simple hex viewer for the terminal. Uses colored output to distinguish different categories of bytes."
content_hash: a49dc3db8ced388bdfc26227a9a7b957ad6bc3a3
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# hexyl

A simple hex viewer for the terminal. Uses colored output to distinguish different categories of bytes.
More information: <https://github.com/sharkdp/hexyl>.

- Print the hexadecimal representation of a file:

`hexyl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Print the hexadecimal representation of the first n bytes of a file:

`hexyl -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Print bytes 512 through 1024 of a file:

`hexyl -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">512</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1024</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Print 512 bytes starting at the 1024th byte:

`hexyl -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1024</span>`:+`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">512</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

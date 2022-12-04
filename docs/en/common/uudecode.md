---
layout: page
title: common/uudecode (English)
description: "Decode files encoded by `uuencode`."
content_hash: 0c7e672111f730283809a5631ab61fd89f004d25
last_modified_at: 2022-12-04
---
# uudecode

Decode files encoded by `uuencode`.
More information: <https://manned.org/uudecode>.

- Decode a file that was encoded with `uuencode` and print the result to `stdout`:

`uudecode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/encoded_file</span>

- Decode a file that was encoded with `uuencode` and write the result to a file:

`uudecode -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/decoded_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/encoded_file</span>

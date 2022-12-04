---
layout: page
title: common/uuencode (English)
description: "Encode binary files into ASCII for transport via mediums that only support simple ASCII encoding."
content_hash: 90474500cdff95c5c9de3435214052d62b99302f
last_modified_at: 2022-12-04
---
# uuencode

Encode binary files into ASCII for transport via mediums that only support simple ASCII encoding.
More information: <https://manned.org/uuencode>.

- Encode a file and print the result to `stdout`:

`uuencode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output_file_name_after_decoding</span>

- Encode a file and write the result to a file:

`uuencode -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output_file_name_after_decoding</span>

- Encode a file using Base64 instead of the default uuencode encoding and write the result to a file:

`uuencode -m -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output_file_name_after_decoding</span>

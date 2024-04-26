---
layout: page
title: common/iconv (English)
description: "Convert text from one encoding to another."
content_hash: 7cfc910e94b63b9e01b6f58e67de091985545fdc
last_modified_at: 2024-04-26
tldri18n_status: 2
---
# iconv

Convert text from one encoding to another.
More information: <https://manned.org/iconv>.

- Convert file to a specific encoding, and print to `stdout`:

`iconv -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">from_encoding</span>` -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">to_encoding</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input_file</span>

- Convert file to the current locale's encoding, and output to a file:

`iconv -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">from_encoding</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input_file</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output_file</span>

- List supported encodings:

`iconv -l`

---
layout: page
title: common/iconv (English)
description: "Converts text from one encoding to another."
content_hash: 405ec57752b7d9c5e61b645955fa81cbffe09764
last_modified_at: 2022-12-04
---
# iconv

Converts text from one encoding to another.
More information: <https://manned.org/iconv>.

- Convert file to a specific encoding, and print to `stdout`:

`iconv -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">from_encoding</span>` -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">to_encoding</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input_file</span>

- Convert file to the current locale's encoding, and output to a file:

`iconv -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">from_encoding</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input_file</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output_file</span>

- List supported encodings:

`iconv -l`

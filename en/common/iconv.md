---
layout: page
title: common/iconv (English)
description: "Converts text from one encoding to another."
content_hash: 10f521ee5fb28f73e97e73664a7039e5845d9d2f
---
# iconv

Converts text from one encoding to another.
More information: <https://manned.org/iconv>.

- Convert file to a specific encoding, and print to stdout:

`iconv -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">from_encoding</span>` -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">to_encoding</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input_file</span>

- Convert file to the current locale's encoding, and output to a file:

`iconv -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">from_encoding</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input_file</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output_file</span>

- List supported encodings:

`iconv -l`

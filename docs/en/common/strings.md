---
layout: page
title: common/strings (English)
description: "Find printable strings in an object file or binary."
content_hash: 71e4ba4518a7a5be7ebd0c5f932604bd1fc622d3
last_modified_at: 2022-12-04
---
# strings

Find printable strings in an object file or binary.
More information: <https://manned.org/strings>.

- Print all strings in a binary:

`strings `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Limit results to strings at least *length* characters long:

`strings -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">length</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Prefix each result with its offset within the file:

`strings -t d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Prefix each result with its offset within the file in hexadecimal:

`strings -t x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

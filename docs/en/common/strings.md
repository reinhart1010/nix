---
layout: page
title: common/strings (English)
description: "Find printable strings in an object file or binary."
content_hash: b2bc7648b8ff9808c6b0eb91121cf5845d613127
---
# strings

Find printable strings in an object file or binary.
More information: <https://manned.org/strings>.

- Print all strings in a binary:

`strings `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>

- Limit results to strings at least *length* characters long:

`strings -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">length</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>

- Prefix each result with its offset within the file:

`strings -t d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>

- Prefix each result with its offset within the file in hexadecimal:

`strings -t x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>

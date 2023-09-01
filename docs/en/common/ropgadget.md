---
layout: page
title: common/ropgadget (English)
description: "Find ROP gadgets in binary files."
content_hash: fbd34a3912d44e8002d3765093175e390e247acb
last_modified_at: 2023-09-01
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># ROPgadget

Find ROP gadgets in binary files.
More information: <https://github.com/JonathanSalwan/ROPgadget>.

- List gadgets in the binary file:

`ROPgadget --binary `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/binary</span>

- Filter gadgets in the binary file by a regular expression:

`ROPgadget --binary `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/binary</span>` --re `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regex</span>

- List gadgets in the binary file, excluding specified type:

`ROPgadget --binary `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/binary</span>` --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">norop|nojob|nosys</span>

- Exclude bad byte gadgets in the binary file:

`ROPgadget --binary `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/binary</span>` --badbytes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">byte_string</span>

- List gadgets up to the specified number of bytes in the binary file:

`ROPgadget --binary `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/binary</span>` --depth `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nbyte</span>

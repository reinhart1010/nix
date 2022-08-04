---
layout: page
title: linux/xed (English)
description: "Edit files in Cinnamon desktop environment."
content_hash: d556b979dcd4e6b32b687277df3899a429543ec3
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># xed

Edit files in Cinnamon desktop environment.
More information: <https://github.com/linuxmint/xed>.

- Start the editor:

`xed`

- Open specific files:

`xed `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>

- Open files using a specific encoding:

`xed --encoding `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">WINDOWS-1252</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>

- Print all supported encodings:

`xed --list-encodings`

- Open a file and go to a specific line:

`xed +`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

---
layout: page
title: linux/loadkeys (English)
description: "Load the kernel keymap for the console."
content_hash: 7a8c74b9b044d9671543395fd8469bde3ae3655c
---
# loadkeys

Load the kernel keymap for the console.
More information: <https://manned.org/loadkeys>.

- Load a default keymap:

`loadkeys --default`

- Load default keymap when an unusual keymap is loaded and `-` sign cannot be found:

`loadkeys defmap`

- Create a kernel source table:

`loadkeys --mktable`

- Create a binary keymap:

`loadkeys --bkeymap`

- Search and parse keymap without action:

`loadkeys --parse`

- Load the keymap suppressing all output:

`loadkeys --quiet`

- Load a keymap from the specified file for the console:

`loadkeys --console `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/ttyN</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/path/to/file</span>

- Use standard names for keymaps of different locales:

`loadkeys --console `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/ttyN</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uk</span>

---
layout: page
title: linux/loadkeys (English)
description: "Load the kernel keymap for the console."
content_hash: 61ab50f06e872e50f0389cc3709adc27a330d90e
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># loadkeys

Load the kernel keymap for the console.
More information: <https://manned.org/loadkeys>.

- Load a default keymap:

`loadkeys --default`

- Create a kernel source table:

`loadkeys --mktable`

- Create a binary keymap:

`loadkeys --bkeymap`

- Search and parse keymap without action:

`loadkeys --parse`

- Load the keymap suppressing all output:

`loadkeys --quiet`

- Display help:

`loadkeys --help`

- Display version:

`loadkeys --version`

---
layout: page
title: common/unimatrix (English)
description: "Simulate the Matrix look with Unicode characters."
content_hash: 8a87dcf4a3a44502a79c238cddf79fa88be23a74
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# unimatrix

Simulate the Matrix look with Unicode characters.
See also: `cmatrix`.
More information: <https://github.com/will8211/unimatrix>.

- Mimic the default output of `cmatrix` (no unicode, works in a TTY):

`unimatrix --no-bold --speed `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">96</span>` --character-list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">o</span>

- No bold characters, slowly, with emojis, numbers, and a few symbols:

`unimatrix --no-bold --speed `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">50</span>` --character-list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ens</span>

- Change the color of characters:

`unimatrix --color `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">red|green|blue|white|...</span>

- Select character set(s) using letter codes (see `unimatrix --help` for available character sets):

`unimatrix --character-list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">character_sets</span>

- Change the scrolling speed:

`unimatrix --speed `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">number</span>

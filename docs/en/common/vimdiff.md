---
layout: page
title: common/vimdiff (English)
description: "Open up two or more files in vim and show the differences between them."
content_hash: e2da6e26d5d1deba3ace0491328934ea461e7175
related_topics:
  - title: español version
    url: /es/common/vimdiff.html
    icon: bi bi-globe
---
# vimdiff

Open up two or more files in vim and show the differences between them.
See also `vim`.
More information: <https://www.vim.org>.

- Open two files and show the differences:

`vimdiff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file2</span>

- Move the cursor to the window on the left|right:

`Ctrl + w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">h|l</span>

- Jump to the next difference:

`[c`

- Jump to the previous difference:

`]c`

- Copy the highlighted difference from the other window to the current window:

`do`

- Copy the highlighted difference from the current window to the other window:

`dp`

- Update all highlights and folds:

`:diffupdate`

- Toggle the highlighted code fold:

`za`

---
layout: page
title: common/most (English)
description: "Open one or several files for interactive reading, allowing scrolling and search."
content_hash: 68ef6227629e1003d9c49de4bd81ef442b21feef
---
# most

Open one or several files for interactive reading, allowing scrolling and search.
More information: <https://manned.org/most>.

- Open a file:

`most `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Open several files:

`most `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file2</span>

- Open a file at the first occurrence of "string":

`most `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>` +/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string</span>

- Move through opened files:

`:O n`

- Jump to the 100th line:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>`j`

- Edit current file:

`e`

- Split the current window in half:

`<CTRL-x> o`

- Exit:

`Q`

---
layout: page
title: common/most (English)
description: "Open one or several files for interactive reading, allowing scrolling and search."
content_hash: b596ebd9b55e9447d892f5dbd84a9836798c5f7b
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# most

Open one or several files for interactive reading, allowing scrolling and search.
More information: <https://manned.org/most>.

- Open a file:

`most `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Open several files:

`most `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file2</span>

- Open a file at the first occurrence of "string":

`most `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` +/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string</span>

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

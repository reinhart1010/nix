---
layout: page
title: common/multitail (English)
description: "Extension of tail."
content_hash: 02f352ce700aa6853b0cf321ad9df253510e8671
---
# multitail

Extension of tail.
More information: <https://manned.org/multitail>.

- Tail all files matching a pattern in a single stream:

`multitail -Q 1 '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pattern</span>`'`

- Tail all files in a directory in a single stream:

`multitail -Q 1 '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">directory</span>`/*'`

- Automatically add new files to a window:

`multitail -Q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pattern</span>

- Show 5 logfiles while merging 2 and put them in 2 columns with only one in the left column:

`multitail -s 2 -sn 1,3 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mergefile</span>` -I `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file3</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file4</span>

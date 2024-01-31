---
layout: page
title: common/multitail (English)
description: "Extension of tail."
content_hash: 6e36dbddc56a1c07e9f2cdf42ebe9211a8a2c1f8
last_modified_at: 2024-01-31
tldri18n_status: 2
---
# multitail

Extension of tail.
More information: <https://manned.org/multitail>.

- Tail all files matching a pattern in a single stream:

`multitail -Q 1 '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pattern</span>`'`

- Tail all files in a directory in a single stream:

`multitail -Q 1 '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>`/*'`

- Automatically add new files to a window:

`multitail -Q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pattern</span>

- Show 5 logfiles while merging 2 and put them in 2 columns with only one in the left column:

`multitail -s 2 -sn 1,3 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/mergefile</span>` -I `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file3</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file4</span>

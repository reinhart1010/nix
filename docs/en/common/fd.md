---
layout: page
title: common/fd (English)
description: "An alternative to `find`."
content_hash: 0b7c2d3b8e188e7a114c7f5459c84fcdcf31ccbd
---
# fd

An alternative to `find`.
Aims to be faster and easier to use than `find`.
More information: <https://github.com/sharkdp/fd>.

- Recursively find files matching the given pattern in the current directory:

`fd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pattern</span>

- Find files that begin with `foo`:

`fd '^foo'`

- Find files with a specific extension:

`fd --extension txt`

- Find files in a specific directory:

`fd '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pattern</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Include ignored and hidden files in the search:

`fd --hidden --no-ignore '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pattern</span>`'`

- Execute a command on each search result returned:

`fd '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pattern</span>`' --exec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

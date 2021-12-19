---
layout: page
title: common/fd (English)
description: "An alternative to `find`."
content_hash: a1fceff331ae326b56ce105d56f1bbac072ffa76
---
# fd

An alternative to `find`.
Aims to be faster and easier to use than `find`.
More information: <https://github.com/sharkdp/fd>.

- Recursively find files matching the given pattern in the current directory:

`fd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pattern</span>

- Find files that begin with "foo":

`fd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'^foo'</span>

- Find files with a specific extension:

`fd --extension `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">txt</span>

- Find files in a specific directory:

`fd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pattern</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Include ignored and hidden files in the search:

`fd --hidden --no-ignore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pattern</span>

- Execute a command on each search result returned:

`fd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pattern</span>` --exec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

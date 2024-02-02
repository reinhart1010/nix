---
layout: page
title: common/ccache (English)
description: "C/C++ compiler cache."
content_hash: 99b33f321fe9a3e1c327a24aeadf9f83e0e9a7a3
last_modified_at: 2024-02-02
tldri18n_status: 2
---
# ccache

C/C++ compiler cache.
Note: packages usually provide symlinks for compilers in `/usr/lib/ccache/bin`. Prepend this directory to `$PATH` to automatically use `ccache` for them.
More information: <https://ccache.dev/manual/latest.html>.

- Show current cache [s]tatistics:

`ccache --show-stats`

- [C]lear all cache:

`ccache --clear`

- Reset ([z]ero) statistics (but not cache itself):

`ccache --zero-stats`

- Compile C code and cache compiled output (to use `ccache` on all `gcc` invocations, see the note above):

`ccache gcc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.c</span>

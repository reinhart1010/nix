---
layout: page
title: common/lsd (English)
description: "List directory contents."
content_hash: ac1b0a0276565439edc11cb478f1e8dc5ca49ff6
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# lsd

List directory contents.
The next generation `ls` command, written in Rust.
More information: <https://github.com/Peltoche/lsd>.

- List files and directories, one per line:

`lsd -1`

- List all files and directories, including hidden ones, in the current directory:

`lsd -a`

- List all files and directories with trailing `/` added to directory names:

`lsd -F`

- List all files and directories in long format (permissions, ownership, size, and modification date):

`lsd -la`

- List all files and directories in long format with size displayed using human-readable units (KiB, MiB, GiB):

`lsd -lh`

- List all files and directories in long format, sorted by size (descending):

`lsd -lS`

- List all files and directories in long format, sorted by modification date (oldest first):

`lsd -ltr`

- Only list directories:

`lsd -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*/</span>

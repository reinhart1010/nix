---
layout: page
title: common/lsd (English)
description: "List directory contents."
content_hash: 6841745311b2d5a0e1d2cb8d8612e88512eb5774
last_modified_at: 2024-09-21
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

- List files and directories with trailing `/` added to directory names:

`lsd -F`

- List all files and directories in long format (permissions, ownership, size in human-readable format, and modification date):

`lsd -lha`

- List files and directories in long format, sorted by size (descending):

`lsd -lS`

- List files and directories in long format, sorted by modification date (oldest first):

`lsd -ltr`

- Only list directories:

`lsd -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*/</span>

- Recursively list all directories in a tree format:

`lsd --tree -d`

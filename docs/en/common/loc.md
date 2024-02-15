---
layout: page
title: common/loc (English)
description: "Count lines of code. Written in Rust."
content_hash: 8e70bee8ab75525b8f873b17a7c7c1ed5557e07a
last_modified_at: 2024-02-15
tldri18n_status: 2
---
# loc

Count lines of code. Written in Rust.
More information: <https://github.com/cgag/loc>.

- Print lines of code in the current directory:

`loc`

- Print lines of code in the target directory:

`loc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Print lines of code with stats for individual files:

`loc --files`

- Print lines of code without .gitignore (etc.) files (e.g. two -u flags will additionally count hidden files and dirs):

`loc -u`

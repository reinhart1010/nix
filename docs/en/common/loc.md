---
layout: page
title: common/loc (English)
description: "Tool written in Rust that counts lines of code."
content_hash: fb244e613473bedd4f437f3e79abc5defca0a0d3
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# loc

Tool written in Rust that counts lines of code.
More information: <https://github.com/cgag/loc>.

- Print lines of code in the current directory:

`loc`

- Print lines of code in the target directory:

`loc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Print lines of code with stats for individual files:

`loc --files`

- Print lines of code without .gitignore (etc.) files (e.g. two -u flags will additionally count hidden files and dirs):

`loc -u`

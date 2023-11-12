---
layout: page
title: common/sk (English)
description: "Fuzzy finder written in Rust."
content_hash: df6157601ec397209d5d14c940b2628d94da28ea
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# sk

Fuzzy finder written in Rust.
Similar to `fzf`.
More information: <https://github.com/lotabout/skim>.

- Start `skim` on all files in the specified directory:

`find `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` -type f | sk`

- Start `skim` for running processes:

`ps aux | sk`

- Start `skim` with a specified query:

`sk --query "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">query</span>`"`

- Select multiple files with `Shift + Tab` and write to a file:

`find `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` -type f | sk --multi > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

---
layout: page
title: common/sk (English)
description: "Fuzzy finder written in Rust."
content_hash: 21b86a4dd748ba10b02949db73a8cb6f0d336a03
---
# sk

Fuzzy finder written in Rust.
Similar to `fzf`.
More information: <https://github.com/lotabout/skim>.

- Start skim on all files in the specified directory:

`find `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` -type f | sk`

- Start skim for running processes:

`ps aux | sk`

- Start skim with a specified query:

`sk --query "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">query</span>`"`

- Select multiple files with `Shift + Tab` and write to a file:

`find `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` -type f | sk --multi > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>

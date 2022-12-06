---
layout: page
title: common/fzf (English)
description: "Command-line fuzzy finder."
content_hash: 5e15f8b4cfee0aeed2a6d420e776d67508194b09
last_modified_at: 2022-12-06
---
# fzf

Command-line fuzzy finder.
Similar to `sk`.
More information: <https://github.com/junegunn/fzf>.

- Start fzf on all files in the specified directory:

`find `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` -type f | fzf`

- Start fzf for running processes:

`ps aux | fzf`

- Select multiple files with `Shift + Tab` and write to a file:

`find `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` -type f | fzf --multi > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Start fzf with a specified query:

`fzf --query "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">query</span>`"`

- Start fzf on entries that start with core and end with either go, rb, or py:

`fzf --query "^core go$ | rb$ | py$"`

- Start fzf on entries that not match pyc and match exactly travis:

`fzf --query "!pyc 'travis"`

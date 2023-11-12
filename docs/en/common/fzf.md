---
layout: page
title: common/fzf (English)
description: "Command-line fuzzy finder."
content_hash: 91445c6f6fa6183d56ad2066f24575c75e896f65
last_modified_at: 2023-11-12
related_topics:
  - title: Türkçe version
    url: /tr/common/fzf.html
    icon: bi bi-globe
tldri18n_status: 2
---
# fzf

Command-line fuzzy finder.
Similar to `sk`.
More information: <https://github.com/junegunn/fzf>.

- Start `fzf` on all files in the specified directory:

`find `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` -type f | fzf`

- Start `fzf` for running processes:

`ps aux | fzf`

- Select multiple files with `Shift + Tab` and write to a file:

`find `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` -type f | fzf --multi > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Start `fzf` with a specified query:

`fzf --query "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">query</span>`"`

- Start `fzf` on entries that start with core and end with either go, rb, or py:

`fzf --query "^core go$ | rb$ | py$"`

- Start `fzf` on entries that not match pyc and match exactly travis:

`fzf --query "!pyc 'travis"`

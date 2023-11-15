---
layout: page
title: common/colordiff (English)
description: "A wrapper around `diff` that produces the same output but with pretty syntax highlighting."
content_hash: 3c5b81ff59e45355d0b2f72c33e74b2b0fc57eaf
last_modified_at: 2023-11-15
related_topics:
  - title: italiano version
    url: /it/common/colordiff.html
    icon: bi bi-globe
tldri18n_status: 2
---
# colordiff

A wrapper around `diff` that produces the same output but with pretty syntax highlighting.
Color schemes can be customized.
More information: <https://github.com/kimmel/colordiff>.

- Compare files:

`colordiff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file2</span>

- Output in two columns:

`colordiff -y `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file2</span>

- Ignore case differences in file contents:

`colordiff -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file2</span>

- Report when two files are the same:

`colordiff -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file2</span>

- Ignore whitespace:

`colordiff -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file2</span>

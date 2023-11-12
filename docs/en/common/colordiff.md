---
layout: page
title: common/colordiff (English)
description: "A tool to colorize diff output."
content_hash: 9cd8ec3da21c482d2346d20b2f2cccdb5bea118e
last_modified_at: 2023-11-12
related_topics:
  - title: italiano version
    url: /it/common/colordiff.html
    icon: bi bi-globe
tldri18n_status: 2
---
# colordiff

A tool to colorize diff output.
The Perl script colordiff is a wrapper for `diff` and produces the same output but with pretty syntax highlighting. Color schemes can be customized.
More information: <https://github.com/kimmel/colordiff>.

- Compare files:

`colordiff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file2</span>

- Output in two columns:

`colordiff -y `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file2</span>

- Ignore case differences in file contents:

`colordiff -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file2</span>

- Report when two files are the same:

`colordiff -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file2</span>

- Ignore white spaces:

`colordiff -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file2</span>

---
layout: page
title: common/xo (English)
description: "A pluggable, zero-configuration linting utility for JavaScript."
content_hash: b50881d412b832e117ed99d1b07f50b17ebe36ee
last_modified_at: 2024-01-31
tldri18n_status: 2
---
# xo

A pluggable, zero-configuration linting utility for JavaScript.
More information: <https://github.com/xojs/xo>.

- Lint files in the "src" directory:

`xo`

- Lint a given set of files:

`xo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1.js path/to/file2.js ...</span>

- Automatically fix any lint issues found:

`xo --fix`

- Lint using spaces as indentation instead of tabs:

`xo --space`

- Lint using the "prettier" code style:

`xo --prettier`

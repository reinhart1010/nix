---
layout: page
title: common/xo (English)
description: "A pluggable, zero-configuration linting utility for JavaScript."
content_hash: c295f055fceff976226e3edd03e8b98b54430326
---
# xo

A pluggable, zero-configuration linting utility for JavaScript.
More information: <https://github.com/xojs/xo>.

- Lint files in the "src" directory:

`xo`

- Lint a given set of files:

`xo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file1</span>`.js `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file2</span>`.js`

- Automatically fix any lint issues found:

`xo --fix`

- Lint using spaces as indentation instead of tabs:

`xo --space`

- Lint using the "prettier" code style:

`xo --prettier`

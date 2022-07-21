---
layout: page
title: osx/cot (English)
description: "The Plain-Text Editor for macOS."
content_hash: 5a982de3df7b97e5b3b83a9acc9a44989594a298
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># cot

The Plain-Text Editor for macOS.
More information: <https://coteditor.com/>.

- Start CotEditor:

`cot`

- Open specific files:

`cot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>

- Open a new blank document:

`cot --new`

- Open a specific file and block the terminal until it is closed:

`cot --wait `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Open a specific file with the cursor at a specific line and column:

`cot --line `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">line_number</span>` --column `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">column_number</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

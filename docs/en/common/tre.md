---
layout: page
title: common/tre (English)
description: "Show the contents of the current directory as a tree."
content_hash: 9edef3fd3419d8c66c63ddac81fd82cf55e4667a
last_modified_at: 2023-07-01
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># tre

Show the contents of the current directory as a tree.
Respects the `.gitignore` settings by default.
More information: <https://github.com/dduan/tre>.

- Print directories only:

`tre --directories`

- Print JSON containing files in the tree hierarchy instead of the normal tree diagram:

`tre --json`

- Print files and directories up to the specified depth limit (where 1 means the current directory):

`tre --limit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">depth</span>

- Print all hidden files and directories using the specified colorization mode:

`tre --all --color `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">automatic|always|never</span>

- Print files within the tree hierarchy, assigning a shell alias to each file that, when called, will open the associated file using the provided `command` (or in `$EDITOR` by default):

`tre --editor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Print files within the tree hierarchy, excluding all paths that match the provided regular expression:

`tre --exclude `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regular_expression</span>

- Display version:

`tre --version`

- Display help:

`tre --help`

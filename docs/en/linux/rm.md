---
layout: page
title: linux/rm (English)
description: "Remove files or directories."
content_hash: b29dc427823722252cc5311432245cb154882e7c
last_modified_at: 2023-01-07
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># rm

Remove files or directories.
See also: `rmdir`.
More information: <https://www.gnu.org/software/coreutils/rm>.

- Remove specific files:

`rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>

- Remove specific files ignoring nonexistent ones:

`rm --force `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>

- Remove specific files interactively prompting before each removal:

`rm --interactive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>

- Remove specific files printing info about each removal:

`rm --verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>

- Remove specific files and directories recursively:

`rm --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory1 path/to/file_or_directory2 ...</span>

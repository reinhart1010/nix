---
layout: page
title: common/ugrep (English)
description: "Ultra fast search tool with query TUI."
content_hash: 7b571f3ef7357cce5582b2e654beaa5e4de4e351
related_topics:
  - title: Deutsch version
    url: /de/common/ugrep.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/ugrep.html
    icon: bi bi-globe
---
# ugrep

Ultra fast search tool with query TUI.
More information: <https://github.com/Genivia/ugrep>.

- Start a query TUI to search files in the current directory recursively (CTRL-Z for help):

`ugrep --query`

- Search the current directory recursively for files containing a regex search pattern:

`ugrep "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_pattern</span>`"`

- Search in a specific file or in all files in a specific directory, showing line numbers of matches:

`ugrep --line-number "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_pattern</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>

- Search in all files in the current directory recursively and print the name of each matching file:

`ugrep --files-with-matches "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_pattern</span>`"`

- Fuzzy search files with up to 3 extra, missing or mismatching characters in the pattern:

`ugrep --fuzzy=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_pattern</span>`"`

- Also search compressed files, `zip` and `tar` archives recursively:

`ugrep --decompress "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_pattern</span>`"`

- Search only files whose filenames match a specific glob pattern:

`ugrep --glob="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">glob_pattern</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_pattern</span>`"`

- Search only C++ source files (use `--file-type=list` to list all file types):

`ugrep --file-type=cpp "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_pattern</span>`"`

---
layout: page
title: linux/rgrep (English)
description: "Recursively find patterns in files using regular expressions."
content_hash: 61433f8520f8303f87110fa7670782c885f5623b
---
# rgrep

Recursively find patterns in files using regular expressions.
Equivalent to `grep -r`.
More information: <https://www.gnu.org/software/grep/manual/grep.html>.

- Recursively search for a pattern in the current working directory:

`rgrep "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_pattern</span>`"`

- Recursively search for a case-insensitive pattern in the current working directory:

`rgrep --ignore-case "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_pattern</span>`"`

- Recursively search for an extended regular expression pattern (supports `?`, `+`, `{}`, `()` and `|`) in the current working directory:

`rgrep --extended-regexp "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_pattern</span>`"`

- Recursively search for an exact string (disables regular expressions) in the current working directory:

`rgrep --fixed-strings "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">exact_string</span>`"`

- Recursively search for a pattern in a specified directory (or file):

`rgrep "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_pattern</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>

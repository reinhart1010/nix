---
layout: page
title: common/fastmod (English)
description: "A fast partial replacement for the codemod tool, replace and replace all in the whole codebase."
content_hash: 806e5b6b36d126e0c4d318526abbd201d44bbf7d
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># fastmod

A fast partial replacement for the codemod tool, replace and replace all in the whole codebase.
Regexes are matched by Rust regex crate.
More information: <https://github.com/facebookincubator/fastmod>.

- Replace a regex pattern in all files of the current directory, ignoring files on .ignore and .gitignore:

`fastmod `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regex_pattern</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">replacement</span>

- Replace a regex pattern in case-insensitive mode in specific files or directories:

`fastmod --ignore-case `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regex_pattern</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">replacement</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file path/to/directory ...</span>

- Replace a regex pattern in in a specific directory files filtered with a case-insensitive glob pattern:

`fastmod `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regex</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">replacement</span>` --dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` --iglob `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'**/*.{js,json}'</span>

- Replace for an exact string in .js or .json files:

`fastmod --fixed-strings `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">exact_string</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">replacement</span>` --extensions `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">json,js</span>

- Replace for an exact string without prompt for a confirmation (disables regular expressions):

`fastmod --accept-all --fixed-strings `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">exact_string</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">replacement</span>

- Replace for an exact string without prompt for a confirmation, printing changed files:

`fastmod --accept-all --print-changed-files --fixed-strings `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">exact_string</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">replacement</span>

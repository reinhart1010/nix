---
layout: page
title: common/rg (English)
description: "Ripgrep is a recursive line-oriented search tool."
content_hash: bdff6254ac956331c2bd604ecf5738acf13bb5fd
last_modified_at: 2023-11-12
related_topics:
  - title: Türkçe version
    url: /tr/common/rg.html
    icon: bi bi-globe
tldri18n_status: 2
---
# rg

Ripgrep is a recursive line-oriented search tool.
Aims to be a faster alternative to `grep`.
More information: <https://github.com/BurntSushi/ripgrep>.

- Recursively search the current directory for a regular expression:

`rg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regular_expression</span>

- Search for regular expressions recursively in the current directory, including hidden files and files listed in `.gitignore`:

`rg --no-ignore --hidden `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regular_expression</span>

- Search for a regular expression only in a subset of directories:

`rg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regular_expression</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">set_of_subdirs</span>

- Search for a regular expression in files matching a glob (e.g. `README.*`):

`rg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regular_expression</span>` --glob `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">glob</span>

- Search for filenames that match a regular expression:

`rg --files | rg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regular_expression</span>

- Only list matched files (useful when piping to other commands):

`rg --files-with-matches `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regular_expression</span>

- Show lines that do not match the given regular expression:

`rg --invert-match `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regular_expression</span>

- Search a literal string pattern:

`rg --fixed-strings -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string</span>

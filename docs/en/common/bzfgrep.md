---
layout: page
title: common/bzfgrep (English)
description: "Find any fixed strings separated by new lines in `bzip2` compressed files using `fgrep`."
content_hash: c7d6513b3e1f63b54d5832a2f6eccfebb75f2e46
last_modified_at: 2024-01-30
tldri18n_status: 2
---
# bzfgrep

Find any fixed strings separated by new lines in `bzip2` compressed files using `fgrep`.
More information: <https://manned.org/bzfgrep>.

- Search for lines matching the list of search strings separated by new lines in a compressed file (case-sensitive):

`bzfgrep "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_string</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Search for lines matching the list of search strings separated by new lines in a compressed file (case-insensitive):

`bzfgrep --ignore-case "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_string</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Search for lines that do not match the list of search strings separated by new lines in a compressed file:

`bzfgrep --invert-match "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_string</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Print file name and line number for each match:

`bzfgrep --with-filename --line-number "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_string</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Search for lines matching a pattern, printing only the matched text:

`bzfgrep --only-matching "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_string</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Recursively search files in a `bzip2` compressed `tar` archive for the given list of strings:

`bzfgrep --recursive "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_string</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

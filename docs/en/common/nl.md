---
layout: page
title: common/nl (English)
description: "A utility for numbering lines, either from a file, or from standard input."
content_hash: 1ee9c4519e381266be1b61b0dae355294f1e1827
last_modified_at: 2022-12-04
---
# nl

A utility for numbering lines, either from a file, or from standard input.
More information: <https://www.gnu.org/software/coreutils/nl>.

- Number non-blank lines in a file:

`nl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Read from standard output:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` | nl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">options</span>` -`

- Number only the lines with printable text:

`nl -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Number all lines including blank lines:

`nl -b a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Number only the body lines that match a basic regular expression (BRE) pattern:

`nl -b p'FooBar[0-9]' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

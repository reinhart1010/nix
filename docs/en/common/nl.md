---
layout: page
title: common/nl (English)
description: "A utility for numbering lines, either from a file, or from standard input."
content_hash: dd3b1180b68748b5639a5238c92a13691bc238f7
---
# nl

A utility for numbering lines, either from a file, or from standard input.
More information: <https://www.gnu.org/software/coreutils/nl>.

- Number non-blank lines in a file:

`nl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>

- Read from standard output:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>` | nl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">options</span>` -`

- Number only the lines with printable text:

`nl -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>

- Number all lines including blank lines:

`nl -b a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>

- Number only the body lines that match a basic regular expression (BRE) pattern:

`nl -b p'FooBar[0-9]' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>

---
layout: page
title: linux/nl (English)
description: "Number lines from a file or from `stdin`."
content_hash: 98341f7e48d005d8fc80cc1de938b8971b1d74c7
last_modified_at: 2024-02-10
tldri18n_status: 2
---
# nl

Number lines from a file or from `stdin`.
More information: <https://manned.org/nl.1p>.

- Number non-blank lines in a file:

`nl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Read from `stdin`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` | nl -`

- Number [a]ll [b]ody lines including blank lines or do not [n]umber [b]ody lines:

`nl --body-numbering `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">a|n</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Number only the [b]ody lines that match a basic regular expression (BRE) [p]attern:

`nl --body-numbering p'FooBar[0-9]' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Use a specific [i]ncrement for line numbering:

`nl --line-increment `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">increment</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Specify the line numbering format to [r]ight or [l]eft justified, keeping leading [z]eros or [n]ot:

`nl --number-format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rz|ln|rn</span>

- Specify the line numbering's width (6 by default):

`nl --number-width `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">col_width</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Use a specific string to separate the line numbers from the lines (TAB by default):

`nl --number-separator `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">separator</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

---
layout: page
title: common/hledger (English)
description: "A plain text accounting software for the command-line."
content_hash: 60e50f919a8b57d6189e438adaf715f46f01d6e1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># hledger

A plain text accounting software for the command-line.
More information: <https://hledger.org>.

- Add transactions to your journal interactively:

`hledger add`

- Show the account hierarchy, using a specific journal file:

`hledger --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.journal</span>` accounts --tree`

- Show a monthly income statement:

`hledger incomestatement --monthly --depth 2`

- Print the amount of cash spent on food:

`hledger print assets:cash | hledger -f- -I balance expenses:food --depth 2`

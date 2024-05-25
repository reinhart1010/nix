---
layout: page
title: common/hledger-add (English)
description: "Record new transactions with interactive prompting in the console."
content_hash: b5b0a46a3ad4115efe4d22b4e6dd76c0e0415f83
last_modified_at: 2024-05-25
tldri18n_status: 2
---
# hledger add

Record new transactions with interactive prompting in the console.
More information: <https://hledger.org/hledger.html#add>.

- Record new transactions, saving to the default journal file:

`hledger add`

- Add transactions to `2024.journal`, but also load `2023.journal` for completions:

`hledger add --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/2024.journal</span>` --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/2023.journal</span>

- Provide answers for the first four prompts:

`hledger add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">today</span>` '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">best buy</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">expenses:supplies</span>` '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$20</span>`'`

- Show `add`'s options and documentation with `$PAGER`:

`hledger add --help`

- Show `add`'s documentation with `info` or `man` if available:

`hledger help add`

---
layout: page
title: common/ledger (English)
description: "A powerful, double-entry accounting system."
content_hash: 9c54b5749dfe383a344ade5e93998c37e613e617
last_modified_at: 2023-11-15
tldri18n_status: 2
---
# ledger

A powerful, double-entry accounting system.
More information: <https://www.ledger-cli.org>.

- Print a balance report showing totals:

`ledger balance --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/ledger.journal</span>

- List all postings in Expenses ordered by amount:

`ledger register `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">expenses</span>` --sorted `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">amount</span>

- Print total Expenses other than Drinks and Food:

`ledger balance `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Expenses</span>` and not (`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Drinks</span>` or `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Food</span>`)`

- Print a budget report:

`ledger budget`

- Print summary information about all the postings:

`ledger stats`

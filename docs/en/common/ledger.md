---
layout: page
title: common/ledger (English)
description: "Ledger is a powerful, double-entry accounting system that is accessed from the UNIX command-line."
content_hash: 18b56976623c7a9c964b1103d296222921435ff5
---
# ledger

Ledger is a powerful, double-entry accounting system that is accessed from the UNIX command-line.
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

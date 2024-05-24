---
layout: page
title: common/hledger (English)
description: "A robust, friendly plain text accounting app."
content_hash: 26f211acb2832bd5ec872b950a7d256a4cc8eb50
last_modified_at: 2024-05-24
tldri18n_status: 2
---
# hledger

A robust, friendly plain text accounting app.
See also: `hledger-ui` for TUI, `hledger-web` for web interface.
More information: <https://hledger.org/hledger.html>.

- Record new transactions interactively, saving to the default journal file:

`hledger add`

- Import new transactions from `bank.csv`, using `bank.csv.rules` to convert:

`hledger import `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/bank.csv</span>

- Print all transactions, reading from multiple specified journal files:

`hledger print --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/prices-2024.journal</span>` --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/prices-2023.journal</span>

- Show all accounts, as a hierarchy, and their types:

`hledger accounts --tree --types`

- Show asset and liability account balances, including zeros, hierarchically:

`hledger balancesheet --empty --tree --no-elide`

- Show monthly incomes/expenses/totals, largest first, summarised to 2 levels:

`hledger incomestatement --monthly --row-total --average --sort --depth 2`

- Show the `assets:bank:checking` account's transactions and running balance:

`hledger aregister assets:bank:checking`

- Show the amount spent on food from the `assets:cash` account:

`hledger print assets:cash | hledger -f- -I aregister expenses:food`

---
layout: page
title: common/hledger-balance (English)
description: "A flexible, general purpose \"summing\" report that shows accounts with some kind of numeric data."
content_hash: 788afda4a6dca1d4063c2aaf17d6521167520d52
last_modified_at: 2024-05-30
tldri18n_status: 2
---
# hledger balance

A flexible, general purpose "summing" report that shows accounts with some kind of numeric data.
This can be balance changes per period, end balances, budget performance, unrealised capital gains, etc.
More information: <https://hledger.org/hledger.html#balance>.

- Show the balance change in all accounts from all postings over all time:

`hledger balance`

- Show the balance change in accounts named `*expenses*`, as a tree, summarising the top two levels only:

`hledger balance `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">expenses</span>` --tree --depth `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>

- Show expenses each month, and their totals and averages, sorted by total; and their monthly budget goals:

`hledger balance `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">expenses</span>` --monthly --row-total --average --sort-amount --budget`

- Similar to the above, shorter form, matching accounts by `Expense` type, as a two level tree without squashing boring accounts:

`hledger bal type:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">X</span>` -MTAS --budget -t -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>` --no-elide`

- Show end balances (including from postings before the start date), quarterly in 2024, in accounts named `*assets*` or `*liabilities*`:

`hledger balance --historical --period '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">quarterly in 2024</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">assets</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">liabilities</span>

- Similar to the above, shorter form; also show zero balances, sort by total and summarise to three levels:

`hledger bal -HQ date:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2024</span>` type:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">AL</span>` -ES -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>

- Show investment assets' market value in base currency at the end of each quarter:

`hledger bal -HVQ `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">assets:investments</span>

- Show unrealised capital gains/losses from market price changes in each quarter, for non-cryptocurrency investment assets:

`hledger bal --gain -Q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">assets:investments</span>` not:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cryptocurrency</span>

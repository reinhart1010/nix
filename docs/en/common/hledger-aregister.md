---
layout: page
title: common/hledger-aregister (English)
description: "Show the transactions and running balances in one account, with each transaction on one line."
content_hash: 099787e311d55800bff5f977cb350efcb1391f6e
last_modified_at: 2024-05-30
tldri18n_status: 2
---
# hledger aregister

Show the transactions and running balances in one account, with each transaction on one line.
More information: <https://hledger.org/hledger.html#aregister>.

- Show transactions and running balance in the `assets:bank:checking` account:

`hledger aregister assets:bank:checking`

- Show transactions and running balance in the first account named `*savings*`:

`hledger aregister savings`

- Show the checking account's cleared transactions, with a specified width:

`hledger aregister checking --cleared --width `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">120</span>

- Show the checking register, including transactions from forecast rules:

`hledger aregister checking --forecast`

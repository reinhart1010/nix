---
layout: page
title: common/hledger-accounts (English)
description: "List account names."
content_hash: 8e5a9cb8307c44020bd113755ff4acc2a7a7952b
last_modified_at: 2024-05-30
tldri18n_status: 2
---
# hledger accounts

List account names.
More information: <https://hledger.org/hledger.html#accounts>.

- Show all accounts used or declared in the default journal file:

`hledger accounts`

- Show accounts used by transactions:

`hledger accounts --used`

- Show accounts declared with account directives:

`hledger accounts --declared`

- Add new account directives, for accounts used but not declared, to the journal:

`hledger accounts --undeclared --directives >> `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2024-accounts.journal</span>

- Show accounts with `asset` in their name, and their declared/inferred types:

`hledger accounts asset --types`

- Show accounts of the `Asset` type:

`hledger accounts type:A`

- Show the first two levels of the accounts hierarchy:

`hledger accounts --tree --depth 2`

- Short form of the above:

`hledger acc -t -2`

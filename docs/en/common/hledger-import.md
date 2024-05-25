---
layout: page
title: common/hledger-import (English)
description: "Import new transactions from one or more data files to the main journal."
content_hash: 45eeb1c48ac7663f9a68fe2e197b427cd31f7729
last_modified_at: 2024-05-25
tldri18n_status: 2
---
# hledger import

Import new transactions from one or more data files to the main journal.
More information: <https://hledger.org/hledger.html#import>.

- Import new transactions from `bank.csv`, using `bank.csv.rules` to convert:

`hledger import `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/bank.csv</span>

- Show what would be imported from these two files, without doing anything:

`hledger import `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/bank1.csv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/bank2.csv</span>` --dry-run`

- Import new transactions from all CSV files, using the same rules for all:

`hledger import --rules-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">common.rules</span>` *.csv`

- Show conversion errors or results while editing `bank.csv.rules`:

`watchexec -- hledger -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/bank.csv</span>` print`

- Mark `bank.csv`'s current data as seen, as if already imported:

`hledger import --catchup `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/bank.csv</span>

- Mark `bank.csv` as all new, as if not yet imported:

`rm -f .latest.bank.csv`

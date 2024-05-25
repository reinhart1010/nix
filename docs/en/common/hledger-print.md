---
layout: page
title: common/hledger-print (English)
description: "Show full journal entries, representing transactions."
content_hash: a75b92c9a8cf5c23e34f8804c1a880ec8f5b0a6e
last_modified_at: 2024-05-25
tldri18n_status: 2
---
# hledger print

Show full journal entries, representing transactions.
More information: <https://hledger.org/hledger.html#print>.

- Show all transactions in the default journal file:

`hledger print`

- Show transactions, with any implied amounts or costs made explicit:

`hledger print --explicit --infer-costs`

- Show transactions from two specified files, with amounts converted to cost:

`hledger print --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/2023.journal</span>` --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/2024.journal</span>` --cost`

- Show `$` transactions in `*food*` but not `*groceries*` accounts this month:

`hledger print cur:\\$ food not:groceries date:thismonth`

- Show transactions of amount 50 or more, with `whole foods` in their description:

`hledger print amt:'>50' desc:'whole foods'`

- Show cleared transactions, with `EUR` amounts rounded and with decimal commas:

`hledger print --cleared --commodity '1000, EUR' --round hard`

- Write transactions from `foo.journal` as a CSV file:

`hledger print --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/foo.journal</span>` --output-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file.csv</span>

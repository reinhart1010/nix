---
layout: page
title: common/ganache-cli (English)
description: "Command-line version of Ganache, your personal blockchain for Ethereum development."
content_hash: edb87f0935bf8134c8e50b7ef208409c48917220
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# ganache-cli

Command-line version of Ganache, your personal blockchain for Ethereum development.
More information: <https://www.trufflesuite.com/ganache>.

- Run Ganache:

`ganache-cli`

- Run Ganache with a specific number of accounts:

`ganache-cli --accounts=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">number_of_accounts</span>

- Run Ganache and lock available accounts by default:

`ganache-cli --secure`

- Run Ganache server and unlock specific accounts:

`ganache-cli --secure --unlock "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">account_private_key1</span>`" --unlock "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">account_private_key2</span>`"`

- Run Ganache with a specific account and balance:

`ganache-cli --account="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">account_private_key</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">account_balance</span>`"`

- Run Ganache with accounts with a default balance:

`ganache-cli --defaultBalanceEther=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">default_balance</span>

- Run Ganache and log all requests to `stdout`:

`ganache-cli --verbose`

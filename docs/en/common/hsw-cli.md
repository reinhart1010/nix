---
layout: page
title: common/hsw-cli (English)
description: "The command-line REST tool for the Handshake wallet."
content_hash: 888e6f727460a47846fdf245e88c0bc2d62b88de
---
# hsw-cli

The command-line REST tool for the Handshake wallet.
More information: <https://github.com/handshake-org/hs-client>.

- Unlock the current wallet (timeout in seconds):

`hsw-cli unlock `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">passphrase</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">timeout</span>

- Lock the current wallet:

`hsw-cli lock`

- View the current wallet's details:

`hsw-cli get`

- View the current wallet's balance:

`hsw-cli balance`

- View the current wallet's transaction history:

`hsw-cli history`

- Send a transaction with the specified coin amount to an address:

`hsw-cli send `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">address</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.05</span>

- View the current wallet's pending transactions:

`hsw-cli pending`

- View details about a transaction:

`hsw-cli tx `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">transaction_hash</span>

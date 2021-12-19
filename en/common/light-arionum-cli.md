---
layout: page
title: common/light-arionum-cli (English)
description: "The PHP light wallet for the Arionum cryptocurrency."
content_hash: f445a409f34c2fe16d73967b21c57be1b9b11d86
---
# light-arionum-cli

The PHP light wallet for the Arionum cryptocurrency.
More information: <https://github.com/arionum/lightWalletCLI>.

- Generate a new public/private key pair:

`light-arionum-cli`

- Display the balance of the current address:

`light-arionum-cli balance`

- Display the balance of the specified address:

`light-arionum-cli balance `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">address</span>

- Send a transaction with an optional message:

`light-arionum-cli send `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">address</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">optional_message</span>

- Export the current wallet information:

`light-arionum-cli export`

- Display information about the current block:

`light-arionum-cli block`

- Display information about the current address' transactions:

`light-arionum-cli transactions`

- Display information about a specific transaction:

`light-arionum-cli transaction `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">transaction_id</span>

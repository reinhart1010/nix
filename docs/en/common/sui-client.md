---
layout: page
title: common/sui-client (English)
description: "Publish smart contracts, get object information, execute transactions, and more."
content_hash: 19f3a059e640642059c63992fea085c7fc795fff
last_modified_at: 2024-10-31
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/sui-client.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># sui client

Publish smart contracts, get object information, execute transactions, and more.
More information: <https://docs.sui.io/references/cli/client>.

- Create a new address with the ED25519 scheme:

`sui client new-address ed25519 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">address-alias</span>

- Create a new testnet environment with an RPC URL and alias:

`sui client new-env --rpc https://fullnode.testnet.sui.io:443 --alias testnet`

- Switch to the address of your choice (accepts also an alias):

`sui client switch --address `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">address-alias</span>

- Switch to the given environment:

`sui client switch --env `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">env-alias</span>

- Publish a smart contract:

`sui client publish `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package-path</span>

- Interact with the Sui faucet:

`sui client faucet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subcommand</span>

- List the gas coins for the given address (accepts also an alias):

`sui client gas `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">address</span>

- Create, sign, and execute programmable transaction blocks:

`sui client ptb `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">options</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subcommand</span>

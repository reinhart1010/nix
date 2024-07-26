---
layout: page
title: common/bitcoin-cli (English)
description: "Command-line client to interact with the Bitcoin Core daemon via RPC calls."
content_hash: e732554a9574b021f4b80e201348d9441d9bbbf4
last_modified_at: 2024-07-26
related_topics:
  - title: italiano version
    url: /it/common/bitcoin-cli.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/bitcoin-cli.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/bitcoin-cli.html
    icon: bi bi-globe
tldri18n_status: 2
---
# bitcoin-cli

Command-line client to interact with the Bitcoin Core daemon via RPC calls.
Uses the configuration defined in `bitcoin.conf`.
More information: <https://en.bitcoin.it/wiki/Running_Bitcoin#Command-line_arguments>.

- Send a transaction to a given address:

`bitcoin-cli sendtoaddress "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">address</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">amount</span>

- Generate one or more blocks:

`bitcoin-cli generate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">num_blocks</span>

- Print high-level information about the wallet:

`bitcoin-cli getwalletinfo`

- List all outputs from previous transactions available to fund outgoing transactions:

`bitcoin-cli listunspent`

- Export the wallet information to a text file:

`bitcoin-cli dumpwallet "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>`"`

- Get blockchain information:

`bitcoin-cli getblockchaininfo`

- Get network information:

`bitcoin-cli getnetworkinfo`

- Stop the Bitcoin Core daemon:

`bitcoin-cli stop`

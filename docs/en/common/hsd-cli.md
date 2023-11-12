---
layout: page
title: common/hsd-cli (English)
description: "The command-line REST tool for the Handshake blockchain."
content_hash: 59163078060f8416c25924dc7288845acdcd5ab9
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# hsd-cli

The command-line REST tool for the Handshake blockchain.
More information: <https://handshake.org>.

- Retrieve information about the current server:

`hsd-cli info`

- Broadcast a local transaction:

`hsd-cli broadcast `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">transaction_hex</span>

- Retrieve a mempool snapshot:

`hsd-cli mempool`

- View a transaction by address or hash:

`hsd-cli tx `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">address_or_hash</span>

- View a coin by its hash index or address:

`hsd-cli coin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hash_index_or_address</span>

- View a block by height or hash:

`hsd-cli block `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">height_or_hash</span>

- Reset the chain to the specified block:

`hsd-cli reset `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">height_or_hash</span>

- Execute an RPC command:

`hsd-cli rpc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">args</span>

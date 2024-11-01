---
layout: page
title: common/sui-client-ptb (English)
description: "Create, sign and execute programmable transaction blocks."
content_hash: e321e161300079ed53d706bfd3deb956ae1ea7c8
last_modified_at: 2024-11-01
tldri18n_status: 2
---
# sui client ptb

Create, sign and execute programmable transaction blocks.
More information: <https://docs.sui.io/references/cli/ptb>.

- Call a Move function from a package and module:

`sui client ptb --move-call p::m::f "<`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">type</span>`>" args`

- Make a Move vector with two elements of type u64:

`sui client ptb --make-move-vec "<u64>" "[1000,2000]"`

- Split a gas coin and transfer it to address:

`sui client ptb --split-coins gas "[1000]" --assign new_coins --transfer-objects "[new_coins]" @`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">address</span>

- Transfer an object to an address:

`sui client ptb --transfer-objects "[`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">object_id</span>`]" @`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">address</span>

- Publish a Move package, and transfer the upgrade capability to sender:

`sui client ptb --move-call sui::tx_context::sender --assign sender --publish "." --assign upgrade_cap --transfer-objects "[upgrade_cap]" sender`

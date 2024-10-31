---
layout: page
title: common/sui-client-faucet (English)
description: "Interact with the Sui faucet."
content_hash: 680dc5be9d0b1dc11d36c488e3029a0ce7b4751f
last_modified_at: 2024-10-31
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/sui-client-faucet.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># sui client faucet

Interact with the Sui faucet.
More information: <https://docs.sui.io/references/cli/client#request-a-sui-coin-from-faucet>.

- Get a SUI coin from the faucet associated with the active network:

`sui client faucet`

- Get a SUI coin for the address (accepts also an alias):

`sui client faucet --address `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">address</span>

- Get a SUI coin from custom faucet:

`sui client faucet --url `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">custom-faucet-url</span>

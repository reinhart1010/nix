---
layout: page
title: common/solcjs (English)
description: "A set of JavaScript bindings for the Solidity compiler."
content_hash: 0a8aa90fd9dfd16e4fd0642a86ae5e599e83af94
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# solcjs

A set of JavaScript bindings for the Solidity compiler.
More information: <https://github.com/ethereum/solc-js>.

- Compile a specific contract to hex:

`solcjs --bin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.sol</span>

- Compile the ABI of a specific contract:

`solcjs --abi `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.sol</span>

- Specify a base path to resolve imports from:

`solcjs --bin --base-path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.sol</span>

- Specify one or more paths to include containing external code:

`solcjs --bin --include-path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.sol</span>

- Optimise the generated bytecode:

`solcjs --bin --optimize `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.sol</span>

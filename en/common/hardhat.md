---
layout: page
title: common/hardhat (English)
description: "A development environment for Ethereum software."
content_hash: d85dd96a58024a16225d3a5c724a70d805f91060
---
# hardhat

A development environment for Ethereum software.
More information: <https://hardhat.org>.

- List available subcommands (or create a new project if no configuration exists):

`hardhat`

- Compile the current project and build all artifacts:

`hardhat compile`

- Run a user-defined script after compiling the project:

`hardhat run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/script.js</span>

- Run Mocha tests:

`hardhat test`

- Run all given test files:

`hardhat test `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1.js</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file2.js</span>

- Start a local Ethereum JSON-RPC node for development:

`hardhat node`

- Start a local Ethereum JSON-RPC node with a specific hostname and port:

`hardhat node --hostname `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hostname</span>` --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>

- Clean the cache and all artifacts:

`hardhat clean`

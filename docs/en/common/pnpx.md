---
layout: page
title: common/pnpx (English)
description: "Directly execute binaries from npm packages, using `pnpm` instead of `npm`."
content_hash: 1286abd91b503c48b949f23ca3abe281e107dcc5
last_modified_at: 2024-10-16
tldri18n_status: 2
---
# pnpx

Directly execute binaries from npm packages, using `pnpm` instead of `npm`.
Note: This command is deprecated! Use `pnpm exec` and `pnpm dlx` instead.
More information: <https://cuyl.github.io/pnpm.github.io/pnpx-cli>.

- Execute the binary from a given npm module:

`pnpx `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">module_name</span>

- Execute a specific binary from a given npm module, in case the module has multiple binaries:

`pnpx --package `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">module_name</span>

- Display help:

`pnpx --help`

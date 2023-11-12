---
layout: page
title: common/pnpx (English)
description: "Directly execute binaries from npm packages, using `pnpm` instead of `npm`."
content_hash: be78395f88c380d2e5013e75673e3112189191af
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# pnpx

Directly execute binaries from npm packages, using `pnpm` instead of `npm`.
More information: <https://pnpm.io/pnpx-cli>.

- Execute the binary from a given npm module:

`pnpx `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">module_name</span>

- Execute a specific binary from a given npm module, in case the module has multiple binaries:

`pnpx --package `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">module_name</span>

- Display help:

`pnpx --help`

---
layout: page
title: common/cargo-fetch (English)
description: "Fetch dependencies of a package from the network."
content_hash: 4268117054fc0fa0b251269ecada8115beff2c73
last_modified_at: 2023-10-30
---
# cargo fetch

Fetch dependencies of a package from the network.
More information: <https://doc.rust-lang.org/cargo/commands/cargo-fetch.html>.

- Fetch dependencies specified in `Cargo.lock` (for all targets):

`cargo fetch`

- Fetch dependencies for the specified target:

`cargo fetch --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">target_triple</span>

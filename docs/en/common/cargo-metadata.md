---
layout: page
title: common/cargo-metadata (English)
description: "Outputs the workspace members and resolved dependencies of current package."
content_hash: d407c7b41702e4dceae2759e1ec6b94e4bd685cc
last_modified_at: 2023-10-22
---
# cargo metadata

Outputs the workspace members and resolved dependencies of current package.
Note: The output format is subject to change in future versions of Cargo.
More information: <https://doc.rust-lang.org/cargo/commands/cargo-metadata.html>.

- Print the workspace members and resolved dependencies of the current package:

`cargo metadata`

- Print only the workspace members and do not fetch dependencies:

`cargo metadata --no-deps`

- Print metadata in a specific format based on the specified version:

`cargo metadata --format-version `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>

- Print metadata with the `resolve` field including dependencies only for the given target triple (Note: the `packages` array will still include the dependencies for all targets):

`cargo metadata --filter-platform `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">target_triple</span>

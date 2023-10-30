---
layout: page
title: common/cargo-metadata (English)
description: "Output the workspace members and resolved dependencies of current package as JSON."
content_hash: cb8a039c79b0e6775565c9b8c4f79f7c5623369c
last_modified_at: 2023-10-30
---
# cargo metadata

Output the workspace members and resolved dependencies of current package as JSON.
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

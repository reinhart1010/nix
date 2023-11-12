---
layout: page
title: common/cargo-tree (English)
description: "Display a tree visualization of a dependency graph."
content_hash: 0c8c1b9fb5d7845d1b3f42707a075d7f2ae2c812
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# cargo tree

Display a tree visualization of a dependency graph.
Note: in the tree, dependencies of packages marked with `(*)` have already been shown elsewhere in the graph, and so are not repeated.
More information: <https://doc.rust-lang.org/cargo/commands/cargo-tree.html>.

- Show a dependency tree of the current project:

`cargo tree`

- Only show dependencies up to the specified depth (e.g. when `n` is 1, display only direct dependencies):

`cargo tree --depth `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>

- Do not display the given package (and its dependencies) in the tree:

`cargo tree --prune `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_spec</span>

- Show all occurrences of repeated dependencies:

`cargo tree --no-dedupe`

- Only show normal/build/development dependencies:

`cargo tree --edges `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">normal|build|dev</span>

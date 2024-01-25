---
layout: page
title: common/cargo-publish (English)
description: "Upload a package to a registry."
content_hash: 0a521a4fa0785b13f15f26a6c50740c78f6e4a3f
last_modified_at: 2024-01-25
tldri18n_status: 2
---
# cargo publish

Upload a package to a registry.
Note: you have to add an authentication token using `cargo login` before publishing a package.
More information: <https://doc.rust-lang.org/cargo/commands/cargo-publish.html>.

- Perform checks, create a `.crate` file and upload it to the registry:

`cargo publish`

- Perform checks, create a `.crate` file but don't upload it (equivalent of `cargo package`):

`cargo publish --dry-run`

- Use the specified registry (registry names can be defined in the configuration - the default is <https://crates.io>):

`cargo publish --registry `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

---
layout: page
title: common/cargo-remove (English)
description: "Remove dependencies from a Rust project's `Cargo.toml` manifest."
content_hash: f310bfea1dfe6820ef91cb1d0ff380cf7f1d99a5
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# cargo remove

Remove dependencies from a Rust project's `Cargo.toml` manifest.
More information: <https://doc.rust-lang.org/cargo/commands/cargo-remove.html>.

- Remove a dependency from the current project:

`cargo remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dependency</span>

- Remove a development or build dependency:

`cargo remove --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dev|build</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dependency</span>

- Remove a dependency of the given target platform:

`cargo remove --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">target</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dependency</span>

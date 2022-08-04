---
layout: page
title: common/cargo-build (English)
description: "Compile a local package and all of its dependencies."
content_hash: b945076558c3a4c6cbb5561f095f4b047fe1c66d
---
# cargo build

Compile a local package and all of its dependencies.
More information: <https://doc.rust-lang.org/cargo/commands/cargo-build.html>.

- Build the package or packages defined by the `Cargo.toml` manifest file in the local path:

`cargo build`

- Build artifacts in release mode, with optimizations:

`cargo build --release`

- Require that `Cargo.lock` is up to date:

`cargo build --locked`

- Build all packages in the workspace:

`cargo build --workspace`

- Build a specific package:

`cargo build --package `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Build only the specified binary:

`cargo build --bin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

- Build only the specified test target:

`cargo build --test `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">testname</span>

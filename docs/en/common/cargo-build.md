---
layout: page
title: common/cargo-build (English)
description: "Compile a local package and all of its dependencies."
content_hash: b945076558c3a4c6cbb5561f095f4b047fe1c66d
last_modified_at: 2023-11-12
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/common/cargo-build.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/cargo-build.html
    icon: bi bi-globe
tldri18n_status: 2
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

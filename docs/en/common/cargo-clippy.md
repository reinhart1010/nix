---
layout: page
title: common/cargo-clippy (English)
description: "A collection of lints to catch common mistakes and improve your Rust code."
content_hash: c26e91822ab6a678d86168b0f1f1fc25b8f647d1
last_modified_at: 2023-11-12
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/common/cargo-clippy.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/cargo-clippy.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cargo clippy

A collection of lints to catch common mistakes and improve your Rust code.
More information: <https://github.com/rust-lang/rust-clippy>.

- Run checks over the code in the current directory:

`cargo clippy`

- Require that `Cargo.lock` is up to date:

`cargo clippy --locked`

- Run checks on all packages in the workspace:

`cargo clippy --workspace`

- Run checks for a package:

`cargo clippy --package `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Treat warnings as errors:

`cargo clippy -- --deny warnings`

- Run checks and ignore warnings:

`cargo clippy -- --allow warnings`

- Apply Clippy suggestions automatically:

`cargo clippy --fix`

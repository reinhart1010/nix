---
layout: page
title: common/cargo-rustc (English)
description: "Compile a Rust package. Similar to `cargo build`, but you can pass extra options to the compiler."
content_hash: 282575de079361564020ecbe3f43c85deb0c6c6d
last_modified_at: 2023-10-30
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/common/cargo-rustc.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/cargo-rustc.html
    icon: bi bi-globe
---
# cargo rustc

Compile a Rust package. Similar to `cargo build`, but you can pass extra options to the compiler.
See `rustc --help` for all available options.
More information: <https://doc.rust-lang.org/cargo/commands/cargo-rustc.html>.

- Build the package and pass options to `rustc`:

`cargo rustc -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rustc_options</span>

- Build artifacts in release mode, with optimizations:

`cargo rustc --release`

- Compile with architecture-specific optimizations for the current CPU:

`cargo rustc --release -- -C target-cpu=native`

- Compile with speed optimizations:

`cargo rustc -- -C opt-level `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1|2|3</span>

- Compile with [s]ize optimizations (`z` also turns off loop vectorization):

`cargo rustc -- -C opt-level `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">s|z</span>

- Check if your package uses unsafe code:

`cargo rustc --lib -- -D unsafe-code`

- Build a specific package:

`cargo rustc --package `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Build only the specified binary:

`cargo --bin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

---
layout: page
title: common/cargo-rustc (English)
description: "Compile a Rust package, and pass extra options to the compiler."
content_hash: 8823175c544dc6479e764f2692406fc5f1c68b45
---
# cargo rustc

Compile a Rust package, and pass extra options to the compiler.
More information: <https://doc.rust-lang.org/cargo/commands/cargo-rustc.html>.

- Build the package or packages defined by the `Cargo.toml` manifest file in the current working directory:

`cargo rustc`

- Build artifacts in release mode, with optimizations:

`cargo rustc --release`

- Compile with architecture-specific optimizations for the current CPU:

`cargo rustc --release -- -C target-cpu=native`

- Compile with speed optimization:

`cargo rustc -- -C opt-level `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1|2|3</span>

- Compile with [s]ize optimization (`z` also turns off loop vectorization):

`cargo rustc -- -C opt-level `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">s|z</span>

- Check if your package uses unsafe code:

`cargo rustc --lib -- -D unsafe-code`

- Build a specific package:

`cargo rustc --package `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Build only the specified binary:

`cargo --bin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

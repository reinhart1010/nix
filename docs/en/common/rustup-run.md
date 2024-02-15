---
layout: page
title: common/rustup-run (English)
description: "Run a command with an environment configured for a Rust toolchain."
content_hash: c41ae75a1440ad155c68ae6b1763aa9eb0400fde
last_modified_at: 2024-02-15
tldri18n_status: 2
---
# rustup run

Run a command with an environment configured for a Rust toolchain.
Note: all commands managed by `rustup` have a shorthand for this: for example, `cargo +nightly build` is equivalent to `rustup run nightly cargo build`.
More information: <https://rust-lang.github.io/rustup>.

- Run a command using a given Rust toolchain (see `rustup help toolchain` for more information):

`rustup run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">toolchain</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

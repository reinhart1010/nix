---
layout: page
title: common/rustup-run (English)
description: "Run a command with an environment configured for a given Rust toolchain."
content_hash: 471eaf7b6bebb72c8fbb154d5627cc9060a1d31a
last_modified_at: 2023-09-17
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># rustup run

Run a command with an environment configured for a given Rust toolchain.
Note: all commands managed by `rustup` have a shorthand for this: for example, `cargo +nightly build` is equivalent to `rustup run nightly cargo build`.
More information: <https://rust-lang.github.io/rustup>.

- Run a command using a given Rust toolchain (see `rustup help toolchain` for more information):

`rustup run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">toolchain</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

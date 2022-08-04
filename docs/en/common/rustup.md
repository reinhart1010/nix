---
layout: page
title: common/rustup (English)
description: "Rust toolchain installer."
content_hash: efab3e4f97632eb7dbc7d6ca0513a808cd44d78e
---
# rustup

Rust toolchain installer.
Install, manage, and update Rust toolchains.
More information: <https://github.com/rust-lang/rustup.rs>.

- Install the nightly toolchain for your system:

`rustup install nightly`

- Switch the default toolchain to nightly so that the `cargo` and `rustc` commands will use it:

`rustup default nightly`

- Use the nightly toolchain when inside the current project, but leave global settings unchanged:

`rustup override set nightly`

- Update all toolchains:

`rustup update`

- List installed toolchains:

`rustup show`

- Run cargo build with a certain toolchain:

`rustup run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">toolchain_name</span>` cargo build`

- Open the local rust documentation in the default web browser:

`rustup doc`

---
layout: page
title: common/rustup (English)
description: "Install, manage, and update Rust toolchains."
content_hash: 7c43b6ce9df4400ff203eba72341bbd53b4f81e2
last_modified_at: 2023-11-12
related_topics:
  - title: தமிழ் version
    url: /ta/common/rustup.html
    icon: bi bi-globe
tldri18n_status: 2
---
# rustup

Install, manage, and update Rust toolchains.
Some subcommands, such as `toolchain`, `target`, `update`, etc. have their own usage documentation.
More information: <https://rust-lang.github.io/rustup>.

- Install the nightly toolchain for your system:

`rustup install nightly`

- Switch the default toolchain to nightly so that the `cargo` and `rustc` commands will use it:

`rustup default nightly`

- Use the nightly toolchain when inside the current project but leave global settings unchanged:

`rustup override set nightly`

- Update all toolchains:

`rustup update`

- List installed toolchains:

`rustup show`

- Run `cargo build` with a certain toolchain:

`rustup run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">toolchain</span>` cargo build`

- Open the local Rust documentation in the default web browser:

`rustup doc`

---
layout: page
title: common/rustup-which (English)
description: "Display which binary will be run for a command managed by `rustup`."
content_hash: 352c4e7c091fe67b7b1f1709214148e0c48bc93b
last_modified_at: 2024-02-15
tldri18n_status: 2
---
# rustup which

Display which binary will be run for a command managed by `rustup`.
Like `which`, but searches a Rust toolchain instead of `$PATH`.
More information: <https://rust-lang.github.io/rustup>.

- Display the path to the binary in the default toolchain:

`rustup which `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Display the path to the binary in the specified toolchain (see `rustup help toolchain` for more information):

`rustup which --toolchain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">toolchain</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

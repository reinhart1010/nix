---
layout: page
title: common/rustup-which (English)
description: "Display which binary will be run for a given command managed by `rustup`."
content_hash: 14371dc6987db2d0635274a65addcbf54abb5f58
last_modified_at: 2023-09-17
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># rustup which

Display which binary will be run for a given command managed by `rustup`.
Like `which`, but searches a Rust toolchain instead of `$PATH`.
More information: <https://rust-lang.github.io/rustup>.

- Display the path to the binary in the default toolchain:

`rustup which `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Display the path to the binary in the specified toolchain (see `rustup help toolchain` for more information):

`rustup which --toolchain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">toolchain</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

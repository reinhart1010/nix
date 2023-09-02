---
layout: page
title: common/rustup-toolchain (English)
description: "Manage Rust toolchains."
content_hash: c160fc36fe3e18ed06b271d2bd655c097dcc5846
last_modified_at: 2023-09-02
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># rustup toolchain

Manage Rust toolchains.
See `rustup help toolchain` for more information about toolchains.
More information: <https://rust-lang.github.io/rustup>.

- Install or update a given toolchain:

`rustup install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">toolchain</span>

- Uninstall a toolchain:

`rustup uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">toolchain</span>

- List installed toolchains:

`rustup list`

- Create a custom toolchain by symlinking to a directory:

`rustup link `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">custom_toolchain_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

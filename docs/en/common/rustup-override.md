---
layout: page
title: common/rustup-override (English)
description: "Modify directory toolchain overrides."
content_hash: 59b9a159881593523f74a25066094285f058b950
last_modified_at: 2023-09-19
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># rustup override

Modify directory toolchain overrides.
See `rustup help toolchain` for more information about toolchains.
More information: <https://rust-lang.github.io/rustup>.

- List directiory toolchain overrides:

`rustup override list`

- Set the override toolchain for the current directory (i.e. tell `rustup` to run `cargo`, `rustc`, etc. from a specific toolchain when in that directory):

`rustup override set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">toolchain</span>

- Remove the toolchain override for the current directory:

`rustup override unset`

- Remove all toolchain overrides for directories that no longer exist:

`rustup override unset --nonexistent`

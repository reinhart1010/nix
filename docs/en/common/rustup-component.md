---
layout: page
title: common/rustup-component (English)
description: "Modify a toolchain's installed components."
content_hash: f3ee0d3469b793bb13e4d53a797b6b626c9127ad
last_modified_at: 2023-09-19
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># rustup component

Modify a toolchain's installed components.
Without the `--toolchain` option `rustup` will use the default toolchain. See `rustup help toolchain` for more information about toolchains.
More information: <https://rust-lang.github.io/rustup>.

- Add a component to a toolchain:

`rustup component add --toolchain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">toolchain</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">component</span>

- Remove a component from a toolchain:

`rustup component remove --toolchain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">toolchain</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">component</span>

- List installed and available components for a toolchain:

`rustup component list --toolchain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">toolchain</span>

- List installed components for a toolchain:

`rustup component list --toolchain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">toolchain</span>` --installed`

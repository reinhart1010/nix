---
layout: page
title: common/cargo-fmt (English)
description: "Run `rustfmt` on all source files in a Rust project."
content_hash: f83fb634b6074f490203b7bebcdd60865e172e70
last_modified_at: 2023-10-01
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># cargo fmt

Run `rustfmt` on all source files in a Rust project.
More information: <https://github.com/rust-lang/rustfmt>.

- Format all source files:

`cargo fmt`

- Check for formatting errors without writing to the files:

`cargo fmt --check`

- Pass arguments to each `rustfmt` call:

`cargo fmt -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rustfmt_args</span>

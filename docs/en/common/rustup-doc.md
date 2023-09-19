---
layout: page
title: common/rustup-doc (English)
description: "Open the offline Rust documentation for the current toolchain."
content_hash: fdc5a3b0a9ffdc3c57f9f074a7d02c6dd367e612
last_modified_at: 2023-09-19
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># rustup doc

Open the offline Rust documentation for the current toolchain.
There are a lot more documentation pages not mentioned here. See `rustup help doc` for more information.
More information: <https://rust-lang.github.io/rustup>.

- Open the main page:

`rustup doc`

- Open the documentation for a specific topic (a module in the standard library, a type, a keyword, etc.):

`rustup doc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">std::fs|usize|fn|...</span>

- Open the Rust Programming Language book:

`rustup doc --book`

- Open the Cargo book:

`rustup doc --cargo`

- Open the Rust Reference:

`rustup doc --reference`

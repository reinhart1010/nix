---
layout: page
title: common/cargo-rustdoc (English)
description: "Generate documentation for the Rust package."
content_hash: 8f8643bf282e217246258ef134fcf1fdd39dfef9
last_modified_at: 2023-10-08
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># cargo rustdoc

Generate documentation for the Rust package.
More information: <https://doc.rust-lang.org/cargo/commands/cargo-rustdoc.html>.

- Open the documentation in the browser:

`cargo rustdoc --open`

- Specify the package to document:

`cargo rustdoc --package `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">spec</span>

- Document the package's library:

`cargo rustdoc --lib`

- Document the specified binary:

`cargo rustdoc --bin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

- Document the specified example:

`cargo rustdoc --example `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

- Document the specified integration test:

`cargo rustdoc --test `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

- Display help:

`cargo rustdoc --help`

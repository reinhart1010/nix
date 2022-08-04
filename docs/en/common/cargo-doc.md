---
layout: page
title: common/cargo-doc (English)
description: "Build and view Rust package documentation offline."
content_hash: 13297bb8ec0c06e4876fc39d31c356a2fc73d7f9
---
# cargo doc

Build and view Rust package documentation offline.
More information: <https://doc.rust-lang.org/cargo/commands/cargo-doc.html>.

- Build and view the default package documentation in the browser:

`cargo doc --open`

- Build documentation without accessing the network:

`cargo doc --offline`

- View a particular package's documentation:

`cargo doc --open --package `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- View a particular package's documentation offline:

`cargo doc --open --offline --package `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

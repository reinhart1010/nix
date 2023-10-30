---
layout: page
title: common/cargo-rustdoc (English)
description: "Build the documentation of Rust packages."
content_hash: a5b3c18c07660743373f192ffb35951407d0200b
last_modified_at: 2023-10-30
---
# cargo rustdoc

Build the documentation of Rust packages.
Similar to `cargo doc`, but you can pass options to `rustdoc`. See `rustdoc --help` for all available options.
More information: <https://doc.rust-lang.org/cargo/commands/cargo-rustdoc.html>.

- Pass options to `rustdoc`:

`cargo rustdoc -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rustdoc_options</span>

- Warn about a documentation lint:

`cargo rustdoc -- --warn rustdoc::`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">lint_name</span>

- Ignore a documentation lint:

`cargo rustdoc -- --allow rustdoc::`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">lint_name</span>

- Document the package's library:

`cargo rustdoc --lib`

- Document the specified binary:

`cargo rustdoc --bin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

- Document the specified example:

`cargo rustdoc --example `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

- Document the specified integration test:

`cargo rustdoc --test `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

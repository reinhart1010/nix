---
layout: page
title: common/rustdoc (English)
description: "Generate documentation for a Rust crate."
content_hash: 8fd3da232e967032aba8e85a215c2e91e4f9c91e
last_modified_at: 2023-10-09
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># rustdoc

Generate documentation for a Rust crate.
More information: <https://doc.rust-lang.org/stable/rustdoc>.

- Generate documentation from the crate's root:

`rustdoc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">src/lib.rs</span>

- Pass a name for the project:

`rustdoc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">src/lib.rs</span>` --crate-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

- Generate documentation from Markdown files:

`rustdoc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.md</span>

- Specify the output directory:

`rustdoc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">src/lib.rs</span>` --out-dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_directory</span>

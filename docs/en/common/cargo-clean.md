---
layout: page
title: common/cargo-clean (English)
description: "Remove generated artifacts in the `target` directory."
content_hash: 6385a2eea0a8fbb57ac3bb8a6761bd4b1e9b2acb
last_modified_at: 2023-10-01
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># cargo clean

Remove generated artifacts in the `target` directory.
More information: <https://doc.rust-lang.org/cargo/commands/cargo-clean.html>.

- Remove the entire `target` directory:

`cargo clean`

- Remove documentation artifacts (the `target/doc` directory):

`cargo clean --doc`

- Remove release artifacts (the `target/release` directory):

`cargo clean --release`

- Remove artifacts in the directory of the given profile (in this case, `target/debug`):

`cargo clean --profile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dev</span>

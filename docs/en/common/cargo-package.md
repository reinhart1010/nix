---
layout: page
title: common/cargo-package (English)
description: "Assemble a local package into a distributable tarball (a `.crate` file)."
content_hash: 50ec282fc4f8d03e212043c01812efeabf4e126b
last_modified_at: 2023-10-31
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># cargo package

Assemble a local package into a distributable tarball (a `.crate` file).
Similar to `cargo publish --dry-run`, but has more options.
More information: <https://doc.rust-lang.org/cargo/commands/cargo-package.html>.

- Perform checks and create a `.crate` file (equivalent of `cargo publish --dry-run`):

`cargo package`

- Display what files would be included in the tarball without actually creating it:

`cargo package --list`

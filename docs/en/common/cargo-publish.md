---
layout: page
title: common/cargo-publish (English)
description: "Upload a package to a registry."
content_hash: a5f4bbe6ae51ae288af06d111ad8cb106c9c35d9
last_modified_at: 2023-10-31
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># cargo publish

Upload a package to a registry.
Note: you have to add an authentication token using `cargo login` before publishing a package.
More information: <https://doc.rust-lang.org/cargo/commands/cargo-publish.html>.

- Perform checks, create a `.crate` file and upload it to the registry:

`cargo publish`

- Perform checks, create a `.crate` file but don't upload it (equivalent of `cargo package`):

`cargo publish --dry-run`

- Specify the name of the registry to use (registry names can be defined in the config - the default is <https://crates.io>):

`cargo publish --registry `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

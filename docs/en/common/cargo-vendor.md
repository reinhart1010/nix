---
layout: page
title: common/cargo-vendor (English)
description: "Vendor all dependencies of a project into the specified directory (default: `vendor`)."
content_hash: 9e191740e599f6ed15390ec645fe33ab15671c9f
last_modified_at: 2023-11-01
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># cargo vendor

Vendor all dependencies of a project into the specified directory (default: `vendor`).
More information: <https://doc.rust-lang.org/cargo/commands/cargo-vendor.html>.

- Vendor dependencies and configure `cargo` to use the vendored sources in the current project:

`cargo vendor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` > .cargo/config.toml`
